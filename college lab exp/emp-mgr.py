from abc import ABC, abstractmethod
import re

# Abstract Class 
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def display_role(self):
        pass


# Classes & Object
class Employee(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def display_role(self):
        print("Role: Employee")


# Inheritance 
class Manager(Employee):

    # Polymorphism 
    def display_role(self):
        print("Role: Manager")


# Regular Expressions 
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# Try–Except 
try:
    name = input("Enter name: ")
    email = input("Enter email: ")
    salary = float(input("Enter salary: "))

   

    # Classes & Objects 
    emp = Employee(name, email, salary)
    mgr = Manager(name, email, salary)

    emp.display_role()
    mgr.display_role()

except ValueError as e:
    print("Error:", e)

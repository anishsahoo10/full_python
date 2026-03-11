class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    def display(self):
        print("name",self.name)
        print("marks",self.marks)

s1=student("ani",90)
s1.display()

#inharitance
class person:
    def greet(self):
        print("hello")
class teacher(person):
    def teach(self):
        print("teaching python")
        
t1=teacher()
t1.greet()
t1.teach()
#polymorphism
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


d = Dog()
c = Cat()

make_sound(d)
make_sound(c)

#try except
def div(a, b):
    return a / b

try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ZeroDivisionError:
    print("Can't divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Execution complete")

#abstract method
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# create object
r = Rectangle(10, 5)

# call method
print("Area:", r.area())
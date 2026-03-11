import re
from abc import ABC, abstractmethod
#abstract class
class LoginSystem(ABC):
    @abstractmethod
    def authenticate(self):
        pass
#child class
class User(LoginSystem):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        correct_username = "Anish"
        correct_password = "1234"

        if self.username == correct_username and self.password == correct_password:
            print("Login Successful")
        else:
            print("Login Failed")
#username
def validate_username(username):
    pattern = r"^[a-zA-Z0-9]{4,10}$"
    if re.match(pattern, username):
        return True
    else:
        return False
#main
try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if validate_username(username):
        user = User(username, password)
        user.authenticate()
    else:
        print("Invalid username format")
except:
    print("Something went wrong")
finally:
    print("Program finished")
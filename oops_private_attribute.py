#private attributes and methods are ment to be used only within the class and are not
#accessible from outside the class
class person:
    __name = "anonymous"
    def __hello(self):
        print("hello")


    def welcome(self):
        self.__hello()
per1 = person()
print(per1.welcome())
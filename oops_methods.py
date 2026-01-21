#methods are functions which belongs to object
class employee:
    def __init__(self,name,sal):
        self.name = name
        self.sal=sal
    def welcome(self):
        print("wlc ",self.name)

e1= employee("coffee",200000)
e1.welcome()

print(e1.name)
print(e1.sal)
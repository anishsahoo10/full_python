class employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal =sal
    def showdetails(self):
        print("name:",self.name,"age:",self.age)
        print("role:",self.role,"dept:",self.dept,"sal:",self.sal)

class engineer(employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("engineer","A",95000)

eng1 = engineer("Anish",18)
eng1.showdetails()
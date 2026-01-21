#method that dont sue self parameter
#class level
class student():
    def __init__(self,name,marks):
        self.name =name
        self.marks = marks
    @staticmethod #decorator
    def hellow():
        print("hello")
    def get_avg(self):
        return sum(self.marks)/len(self.marks)
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hellow",self.name,"ur avg fucking marks is :",sum/3)


s1 = student("gg",[100,100,100])
print(s1.get_avg())
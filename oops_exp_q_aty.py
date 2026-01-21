class student():
    def __init__(self,name,marks):
        self.name =name
        self.marks = marks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hellow",self.name,"ur avg fucking marks is :",sum/3)


s1 = student("gg",[100,100,100])
print(s1.get_avg())
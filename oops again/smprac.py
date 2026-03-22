class student:
    def __init__(self, name ,age,marks ):
        self.name= name
        self.age=age
        self.marks=marks
    
    def display_std(self):
        print("name",self.name,"age",self.age,"marks",self.marks)


s1=student("anish",19,100)
s1.display_std()
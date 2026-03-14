class student:
    def __init__(self,name,phy,chem,maths):
        self.name = name
        self.phy = phy
        self.chem =chem
        self.maths = maths
    def get_average(self):
        return (self.phy+self.chem+self.maths)/3
    

s1 = student("anish",90,88,100)
print(s1.get_average())
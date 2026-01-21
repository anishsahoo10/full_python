class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
       # self.percentage= str((self.phy+self.chem+self.math)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

s1 = student(90,90,90)
print(s1.percentage)

s1.phy =95
print(s1.percentage)
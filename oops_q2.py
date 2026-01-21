class circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return 3.14*self.r*self.r
    def perimeter(self):
        return 2*3.14*self.r

c1= circle(21)
print(c1.area())
print(c1.perimeter())
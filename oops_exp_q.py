class student:
    def __init__(self,name,s1,s2,s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    def avg(self):
        return (self.s1 + self.s2 + self.s3) / 3

s1 = student("ani",12,32,45)
print(s1.avg())

class student():
    #aattributes
    clg_name = "abc college" #class attr
    df_name = "anonymous"
    def __init__(self,name,age): #parameterized constructor
        self.name=name #object attr (diff values for all )
        self.age=age # object attr
        print("data added.......")

s1 = student("anish",18)
print(s1.name)
print(s1.age)
s2 = student("neon",17)
print(s2.name)
print(s2.age)
print(s2.clg_name)
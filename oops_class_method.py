class person:
    name = "anu"
    @classmethod
    def change_name(cls,name):
        cls.name = name

p1 = person()
print(p1.name)
p1.change_name("hehe boi")
print(p1.name)
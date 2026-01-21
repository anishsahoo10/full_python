class car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class bmw(car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
car1 = bmw("bmw","EV")
print(car1.name)
print(car1.type)
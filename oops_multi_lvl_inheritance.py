
class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class bmw(car):
    def __init__(self,name):
        self.name = name

class bmwx1(bmw):
    def __init__(self,type):
        self.type = type

car1 = bmwx1("EV")
print(car1.type)
car1.start()
car1.stop()

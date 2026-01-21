#when one class derives the properties and methods of another class
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

car1 = bmw("x1")
car1.start()

#hiding the implementation of a class  and only showing the essential details to the user
class car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False
    def start_the_car(self):
        self.acc = True
        self.clutch = True
        self.brk = True
        print("car started......vroom vroomm")

car1 = car()
car1.start_the_car()
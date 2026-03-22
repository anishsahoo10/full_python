class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def show_car(self):
        return f"{self.brand} {self.model}"
    
c1 = car("bmw","X1")
print(c1.show_car())
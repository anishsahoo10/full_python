#when a same operator is allowed to have different meaning according to the context
#we have to use fucking dunder function >> double underscore "__add__" these kinda shi
class complex:
    def __init__(self,real,img):
        self.real =real
        self.img =img

    def shownum(self):
        print(self.real,"i+",self.img,"j")
        #addition
    def __add__(self,c2):
        newreal = self.real + c2.real
        newimg = self.img + c2.img
        return complex(newreal,newimg)
        #substraction
    def __sub__(self,c2):
        newreal = self.real - c2.real
        newimg = self.img - c2.img
        return complex(newreal,newimg)

c1 = complex(2,5)
c1.shownum()
c2 = complex(1,2)
c2.shownum()
c3 = c1+c2
c3.shownum()
c4 = c1-c2
c4.shownum()
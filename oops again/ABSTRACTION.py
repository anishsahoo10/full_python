class car:
    def __init__(self):
        self.acc = False
        self.brk = False

    def start(self):
         self.acc = True
         self.brk = True 
         print("car started")
        
c1 = car()
c1.start()
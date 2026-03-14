class acc:
    def __init__(self,bal,acc_no):
        self.bal = bal
        self.acc_no = acc_no

    def debit(self,amount):
        self.bal -=amount
        print("rs",amount,"was debited")
    def credit(self,amount):
        self.bal+=amount
        print("rs", amount, "was credited")
    def display(self):
        print(self.bal)
    
ac1 = acc(20000,124)
ac1.debit(1000) 
ac1.credit(500)     
ac1.display()


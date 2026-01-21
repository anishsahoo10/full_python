class b_account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount):
        self.balance -=amount
        print(amount,"was debited,,,, current balance ",self.balance)
    def credit(self,amount):
        self.balance+=amount
        print(amount,"credited,,, current balance",self.balance)
    def print_balance(self):
        print("ur balance",self.balance)


acc1 = b_account(1000,1234)
deb = acc1.debit(200)
cre  = acc1.credit(900)
bal = acc1.print_balance()


class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,odr):
        return self.price>odr.price

order1=order("chips",20)
order2=order("coffee",25)
print(order1>order2)
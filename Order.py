    
from orderitem import OrderItem
from payment import Payment
import datetime

class Order():
    def __init__(self):
        self.orderitems = []
        self.date = datetime.datetime.now()

    def addOrderItems(self, orderitem):
        self.orderitems.append(orderitem)

    def getOrderItems(self):
        return self.orderitems

    def calcTotal(self):
        total=0.0
        for o in self.orderitems:
            total += o.getItem().itemprice * o.quantity
        payment=Payment(total)
        return payment

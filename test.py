import unittest
from orderitem import OrderItem
from order import Order


class ItemTest(unittest.TestCase):
    def setUp(self):
        self.orderitem=OrderItem(1,'item1', 30.00)
    
    def test_string(self):
        self.assertEqual(str(self.orderitem), self.order.ordername)

    def test_GetItemNumber(self):
        self.assertEqual(self.item.getItemNumber(),1)

    def test_GetItemPrice(self):
        self.assertEqual(self.item.getItemPrice(),30.00)

class OrderItemTest(unittest.TestCase): 
    def setUp(self):
        self.item=Item(1,'item1', 30.00)
        self.oitem=OrderItem(self.item,2)

    def test_Quantity(self):
        self.assertEqual(self.oitem.getQuantity(),2)
    
    def test_item(self):
        item=self.oitem.getItem()
        self.assertEqual(str(item), 'item1')

class OrderTest(unittest.TestCase):
    def setUp(self):
        self.item1=Item(1,'beer',6.25)
        self.item2=Item(2,'chips', 4.50)

        self.orderitem1=OrderItem(self.item1,2)
        self.orderitem2=OrderItem(self.item2,1)

        self.order=Order()
        self.order.addOrderItems(self.orderitem1)
        self.order.addOrderItems(self.orderitem2)

    def test_CalculateTotal(self):
        payment=self.order.calcTotal()
        self.assertEqual(str(payment), 'Your payment today will be 17.0')

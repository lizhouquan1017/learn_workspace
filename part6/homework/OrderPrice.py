# coding:utf-8
from part6.homework.GoodPrice import Product


class Order:
    def __init__(self, id, type, price):
        self.id = id
        self.tpye = type
        self.price = price

    def show_order(self):
        print(self.price)


if __name__ == '__main__':
    p1 = Product(100,2)
    p2 = Product(200,1)
    price = p1.goodsPrice()+p2.goodsPrice()
    o = Order(1,0,price)
    o.show_order()
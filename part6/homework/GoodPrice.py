# coding:utf-8


class Product:
    '''构造方法'''
    def __init__(self, sjdj, num):
        self.sjdj = sjdj
        self.num = num

    '''单个商品价格'''
    def goodsPrice(self):
        return self.sjdj * self.num


if __name__ == '__main__':
    p1 = Product(100, 2)
    p2 = Product(150, 3)
    print(p1.goodsPrice())

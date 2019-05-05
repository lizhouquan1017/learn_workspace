# coding:utf-8

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':
    # 创建一个item对象，将变量赋值给im
    im = Item('鼠标', 29.8)
    # 打印im对象
    print(im)

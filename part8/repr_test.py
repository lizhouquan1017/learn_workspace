# coding:utf-8


class Apple:
    # 实现构造器
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    # 重写__repr__()方法
    def __repr__(self):
        return "Apple[color = "+ self.color+" , weight = " + str(self.weight) + "]"


if __name__ == '__main__':
    a = Apple('red', 25.8)
    print(a)


# coding:utf-8


class Fibs:
    def __init__(self, len):
        self.first = 0
        self.second = 1
        self.__len = len

    # 定义迭代器所需的__next__方法
    def __next__(self):
        # 如果 __len__ 属性为0，则迭代结束
        if self.__len == 0 :
            raise StopIteration
        # 完成数列计算
        self.first, self.second = self.second, self.second+self.first
        # 数列长度减1
        self.__len -= 1
        return self.first

    # 定义__iter__方法，返回方法的迭代器
    def __iter__(self):
        return self


if __name__ == '__main__':
    # 创建fibs对象
    fibs = Fibs(10)
    print(next(fibs))
    for el in fibs:
        print(el, end=' ')

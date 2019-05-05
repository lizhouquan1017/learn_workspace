# coding:utf-8

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        print('-----设置%s属性---' %key)
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, name):
        print('-----读取%s属性---' %name)
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError

    def __delattr__(self, name):
        print('------删除%s属性----' %name)
        if name == 'size':
            self.__dict__['width'] = 0
            self.__dict__['height'] = 0


if __name__ == '__main__':
    rect = Rectangle(3,4)
    print(rect.size)
    rect.size = 6,8
    print(rect.width)
    print(rect.size)

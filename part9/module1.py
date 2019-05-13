# coding:utf-8


print('这是module1')
my_book = '疯狂的Python讲义'


def say_hi(user):
    print('%s , 你好，欢迎学习Python' %user)


class User:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print('%s 正在慢慢地走路' %self.name)

    def __repr__(self):
        return 'User[name = %s]' %self.name

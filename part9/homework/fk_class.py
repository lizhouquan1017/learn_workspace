# coding:utf-8
'''
这是fk_class模块：
Teacher: 代表老师的类
Student: 代表学生的类
Computer: 代表电脑的类
'''


class Teacher(object):
    '''
    定义代表老师的类
    '''

    def teach(self, content):
        print('老师正在教育%s' % content)


class Student(object):
    '''
    定义代表学生的类
    '''

    def learn(self, content):
        print('学生正在学%s' % content)


class Computer(object):
    '''
    定义代表电脑的类
    '''

    def run(self, program):
        print('电脑正在运行%s' % program)

# coding:utf-8


def check_key(key):
    '''
    该函数将会负责检查序列索引，该索引必须是整数值，否则引发TypeError异常
    且程序要求索引必须为非负整数，否则引发IndexError异常
    :param key:
    :return:
    '''
    if not isinstance(key, int):raise TypeError('索引值必须为整数')
    if key < 0 :raise IndexError('索引值必须为非负数')
    if key >26**3 : raise IndexError('索引值不能超过%d' %26**3)


class StringSeq:
    def __init__(self):
        # 用于存储被修改的数据
        self.__changed = {}
        # 用于存储已经删除元素的索引
        self.__deleted = []

    def __len__(self):
        return 26**3

    def __getitem__(self, key):
        '''
        根据索引获取元素的位子
        '''
        check_key(key)
        # 如果在self.__changed中找到修改后的数据
        if key in self.__changed:
            return self.__changed[key]
        # 如果在self.__deleted中，说明该元素已经被删除
        if key in self.__deleted:
            return None
        # 根据计算规则来返回序列元素
        three = key//(26*26)
        two = (key - three*26*26) // 26
        one = key % 26
        return chr(65+three) + chr(65+two)+ chr(65+one)
























# coding:utf-8


def fn(tp):
    for e in tp:
        if not isinstance(e,str):
            raise ValueError('所有元素必须为字符串')
        if not(20>=len(e)>=5):
            raise ValueError('字符串长度符合要求，必须在5~20之间')
    print(tp)


if __name__ == '__main__':
    fn(('fkjava', 'carizyit'))
    fn((20,))

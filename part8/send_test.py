# coding:utf-8


def square_gen(val):
    i = 0
    out_val = None
    while True:
        # 使用yield语句生成值，使用out_val接收send()方法的参数值
        out_val = (yield out_val**2) if out_val is not None else (yield i ** 2)
        # 如果程序使用send()方法获取下一个值，val_out会获取send方法的参数值
        if out_val is not None : print('=====%d' % out_val)
        i += 1


if __name__ == '__main__':
    sg = square_gen(5)
    # 第一次调用send方法获取值，只能传入None
    print(sg.send(None))
    print(next(sg))
    print('-------------')
    print(sg.send(9))
    print(next(sg))
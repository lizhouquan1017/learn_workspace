# coding:utf-8


def test(val,step):
    print('----函数开始执行-----')
    cur = 0
    # 遍历 0 ~ val
    for i in range(val):
        # cur 添加 i*step
        cur += i * step
        yield cur


if __name__ == '__main__':
    t = test(10, 2)
    print(next(t))
    print(next(t))

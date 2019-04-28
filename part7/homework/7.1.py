# coding:utf-8

str_n = input('请输入整数:')
try:
    n = int(str_n)
    print(n)
    i = 0
    while True:
        try:
            a, b = input('请输入2个整数(空格隔开)').split()
            print(int(a)//int(b))
            i += 1
            if i >= n : break
        except:
            print('请输入空格隔开2个整数')
except:
    print('请输入整数N')


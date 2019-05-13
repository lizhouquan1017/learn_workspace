# coding:utf-8


def factorial_generator(n):
    result_list = [1]
    for i in range(2,n+1):
        result_list.append(result_list[-1]*i)
    print('-------------',len(result_list))
    for i in range(n):
        yield result_list[i]


if __name__ == '__main__':
    fg = factorial_generator(10)
    print(next(fg)) # 1，生成器“冻结”在yield处
    print(next(fg)) # 2，生成器再次“冻结”在yield处
    for ele in fg:
        print(ele, end=' ')

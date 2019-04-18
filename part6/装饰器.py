# coding = utf-8


def foo(fn):
    # 定义一个嵌套函数
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n*(n-1))
        print(fn.__name__)
        fn(n*(n-1))
        print("*"*15)
        return fn(n*(n-1))
    return bar


'''
下面的装饰效果相当于foo(my_test)
my_test将会被替代成该语句的返回值
由于foo(fn)返回bar函数，因此funB就是bar
'''

@foo
def my_test(a):
    print("====my_test函数=====")


print(my_test)
my_test(10)
my_test(6, 5)

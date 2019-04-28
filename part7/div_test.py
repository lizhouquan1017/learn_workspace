# coding:utf-8


import sys
try :
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    c = a/b
    print('输入a和b的相除结果：',c)

except IndexError:
    print('输入的参数不够')
except ValueError:
    print('程序只能接受整数参数')
except ArithmeticError:
    print('算术错误')
except Exception:
    print('未知异常')

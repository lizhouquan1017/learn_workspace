s = input('请输入除数:')

try:
    result = 20/int(s)
    print('20除以%s的结果是：%g' %(s, result))
except ValueError:
    print('值错误，请重新输入')
except ArithmeticError:
    print('算数错误，不能输入0')
else:
    print('正常结束')

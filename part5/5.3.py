# 判断闰年方法


def is_year(year):
    year = int(year)
    if (year%4 ==0) and (year%100 != 0):
        return True
    elif (year%400 == 0):
        return True
    else:
        return False


while True:
    year = input('请输入闰年：')
    if year == 'exit':
        import sys
        sys.exit(0)
    print("%s是闰年吗？%s" %(year,is_year(year)))


def fn(n):
    result_list = [1]
    for i in range(n):
        result_list.append(result_list[-1] * len(result_list))
    return result_list[-1]

n = int(input("请输入数字:"))
result = fn(n)
print("%d的阶乘是%d" % (n, result))
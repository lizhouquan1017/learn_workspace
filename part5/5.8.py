import random

def fn(n):
    i, tmp_list = 0, []
    while True:
        num = random.randint(0, 100)
        # 如果随机数不包含在列表中，则保存
        if num not in tmp_list:
            tmp_list.append(num)
            i += 1
        if i == n:
            break
    # 将列表转成元组返回
    return tuple(tmp_list)
n = int(input("请输入整数n:"))
print(fn(n))
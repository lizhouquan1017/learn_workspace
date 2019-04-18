def fn(n):
    sum = 0
    if n == 1:
        return 12
    else:
        return fn(n-1)*1.05


def sum(n):
    num = 0
    for i in range(1, n+1):
        num += fn(i)
    return num

print(sum(20))
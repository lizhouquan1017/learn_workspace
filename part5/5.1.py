# 列表的排序


def list_sort(list):
    list_len = len(list)
    for i in range(0, list_len):
        for j in range(i + 1, list_len):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]


list1 = [3, 6, 8, 10, -1, 299, 32, 60]
list_sort(list1)
print(list1)



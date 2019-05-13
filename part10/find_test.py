import re
# 返回所有匹配的pattern的子串所组成的列表
print(re.findall('fkit', 'FKit is very good ,fkit.org is my favorite', re.I))
# 返回所有匹配pattern的子串所组成的迭代器，忽略大小写
it = re.finditer('fkit', 'FKit is very good ,fkit.org is my favorite', re.I)
for e in it:
    print(str(e.span()) + "-->" + e.group())

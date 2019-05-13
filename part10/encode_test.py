# coding:utf-8

import json
# 将python对象转化为json字符串（元祖会被当成数组）
s = json.dumps(['yuekk',{'favorite':('coding',None,'game',25)}])
print(s)
# 将简单的python字符串转化为json对象
s2 = json.dumps("\"foo\bar")
print(s2)
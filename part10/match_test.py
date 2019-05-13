# coding:utf-8

import re

m1 = re.match('www', 'www.fkit.org')  # 从来时位子匹配

print(m1.span())  # span 返回匹配位置
print(m1.group())  # group 返回匹配的组
print(re.match('fkit', 'www.fkit.org'))  # 从开始位子匹配不到就返回None

m2 = re.search('www', 'www.fkit.org')  # 从开始位子匹配
print(m2.span())  # span 返回匹配位置
print(m2.group())  # group 返回匹配的组

m3 = re.search('fkit', 'www.fkit.org')  # 从中间位子匹配
print(m3.span())  # span 返回匹配位置
print(m3.group())  # group 返回匹配的组

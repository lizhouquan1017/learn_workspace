# coding:utf-8

import re
# 使用逗号对字符串进行分割
print(re.split(',', 'fkit, fkjava, crazyit'))
# 指定值分割一次，被分割成2个字符串
print(re.split(',', 'fkit, fkjava, crazyit', 1))
# 使用a进行分割
print(re.split('a', 'fkit, fkjava, crazyit'))
# 使用x进行分割，没有匹配内容
print(re.split('x', 'fkit, fkjava, crazyit'))

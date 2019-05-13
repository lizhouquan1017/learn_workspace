import random
# 生成0.0到1.0的随机浮点数
print(random.random())
# 生成2.5到10.0的伪随机浮点数
print(random.uniform(2.5,10.0))
# 生成指数分布的伪随机浮点数
print(random.expovariate(1/5))
# 生成0到9的伪随机数
print(random.randrange(10))
# 生成0到100的伪随机偶数
print(random.randrange(0,101,2))
# 随机抽取一个元素
print(random.choice(['Python','java','Swift']))
book_list = ['Python','java','Swift']
# 对列表进行随机排序
random.shuffle(book_list)
print(book_list)
# 随机抽取4个元素
print(random.sample([10,20,30,40,50,60,70,80], k=4))
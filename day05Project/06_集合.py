# 定义空集合只能使用set()
set1 = set()
print(type(set1))
set2 = {}
print(type(set2))

# 定义一个有数据的集合
set3 = {20, 30, 10, 20, 5, 5}
print(set3)  # 去除了重复数据
print(type(set3))

# set()可以把其他类型的数据转换成集合，比如字符串
set4 = set('abcdefg')
print(set4)
print(type(set4))

# 集合中元素的访问：由于集合中的数据没有顺序，所以其没有索引下标，数据的访问有两种方案
# ① 直接打印
# ② 使用for循环对其进行遍历操作（只能使用for循环）
set3 = {20, 30, 10, 20, 5, 5}
for i in set3:
    print(i)

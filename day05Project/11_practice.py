# ------------------------------------------------------------1
# 有一个空字典dict1 = {}，请给他添加一个为name:python的键值对
dict1 = {}
dict1['name'] = 'python'
print(dict1)

# ------------------------------------------------------------2
# 现有字典dict1 = {'name':'python'}，将键为'name'的值更改为'linux'
dict1 = {'name': 'python'}
dict1['name'] = 'linux'
print(dict1)

# ------------------------------------------------------------3
# 请创建一个空集合set1
set1 = set()
print(type(set1))

# ------------------------------------------------------------4
# 有一个集合set1 = {1,2,3,4}
# 请实现：给set1添加一个元素5
set1 = {1, 2, 3, 4}
set1.add(5)
print(set1)

# ------------------------------------------------------------5
# 现有字典dict1 = {'name':'chuanzhi','age':18}
# 要求：1.删除age：18这个键值对
dict1 = {'name': 'chuanzhi', 'age': 18}
del dict1['age']
print(dict1)

# ------------------------------------------------------------6
# 现有字典dict1 = {'name':'chuanzhi','age':18}
# 要求：1.使用循环将字典中所有的键输出到屏幕上
#     2.使用循环将字典中所有的值输出到屏幕上
#     3.使用循环将字典中所有的键值对输出到屏幕上
#       输出方式：  name：chuanzhi
#                  age:18
dict1 = {'name': 'chuanzhi', 'age': 18}
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)
for key, value in dict1.items():  # 提取键值对分别存储在两个变量中
    print(f'{key}:{value}')

# ------------------------------------------------------------7
# 有这样的一个列表
# product=[
# {"name":"电脑","price":7000},
# {"name":"鼠标","price":30},
# {"name":"usb电动小风扇","price":20},
# {"name":"遮阳伞","price":50},
# ]，然后小明一共有8000块钱，那么他能不能买下这所有商品？
# 如果能，请输出“能”，否则输出“不能”
product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]
sum_price = 0
for i in product:
    sum_price += i['price']  # 提取price键的值
print(sum_price)
if sum_price >= 8000:
    print('不能')
else:
    print('能')

# ------------------------------------------------------------8
# 有一个集合set1 = {1,2,3,4}
# 请实现：删除集合中的任意一个元素,注：不是随机删除
set1 = {1,2,3,4}
set1.pop()  # pop后面的括号里面什么都不用写，默认删除第一个元素
print(set1)
# 或者
set1 = {1,2,3,4}
set1.remove(2)  #remove()括号中是可以任意的一个元素值


# ------------------------------------------------------------9
# 有一个集合list1 = [1,2,3,4,3]
# 请完成去重复的功能，并且最后依然是列表
list1 = [1,2,3,4,3]
set1 = set(list1)
list2 = list(set1)
print(list2)

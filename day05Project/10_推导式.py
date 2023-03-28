# 使用while循环创建一个0-9的列表
i = 0
list1 = []
while i <= 9:
    list1.append(i)
    i += 1
print(list1)
# 使用for循环创建一个0-9的列表
list2 = []
for i in range(10):
    list2.append(i)
print(list2)
# 使用推导式创建
list3 = [i for i in range(10)]
print(list3)

# 求0-9之间的偶数
list4 = []
for i in range(10):
    if i % 2 == 0:
        list4.append(i)
print(list4)
# 推导式
list5 = [i for i in range(10) if i % 2 == 0]
print(list5)

# 案例2:有一个列表,里面内容为[1, 2, 3, 4, 5],通过Python代码将其转换为[1, 4, 9, 16, 25]
list6 = [1, 2, 3, 4, 5]
list7 = []
for i in list6:
    list7.append(i ** 2)
print(list7)
# 推导式实现
list8 = [i ** 2 for i in list6]
print(list8)
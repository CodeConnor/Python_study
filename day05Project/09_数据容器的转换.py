# 元组 -> 列表
tuple1 = (1, 2, 3, 4)
list1 = list(tuple1)
print(list1)
# 集合 -> 列表
set1 = {10, 20, 20, 30, 40}  # 去重了
list2 = list(set1)
print(list2)
# 列表 -> 元组
list3 = ['Tom', 'Connor', 'John', 'Jerry']
tuple2 = tuple(list3)
print(tuple2)
# 集合 -> 元组
set2 = {'a', 'b', 'c', 'd'}
tuple3 = tuple(set2)
print(tuple3)
# 列表 -> 集合
list4= [1, 3, 5, 7, 7, 7, 9]
set3 = set(list4)  # 去重
print(set3)
# 元组 -> 集合
tuple4 = ('a', 'b', 'c', 'd', 'a', 'e', 'b')
set4 = set(tuple4)
print(set4)

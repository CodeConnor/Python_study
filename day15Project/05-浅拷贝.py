# 导入模块
import copy

list1 = [1, 3, 5, [7, 9]]
# 拷贝list1
list2 = copy.copy(list1)
list1.append(11)
list1[3].append(9)
print(list1)
print(list2)
# 第一层对象地址不同，对list1
print(id(list1))
print(id(list2))
# 第二层对象地址相同，即证明了浅拷贝只能拷贝最外层对象
print(id(list1[3]))
print(id(list2[3]))

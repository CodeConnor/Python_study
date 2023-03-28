# 定义一个只含一个元素的元组（特殊）
tuple1 = (10,)  # 如果定义的元组是一个单元素元组，则最后必须保留一个逗号，否则定义的就不是元组类型了！
print(type(tuple1))
tuple0 = (10)
print(type(tuple0))

# 多元素元组
tuple2 = (10, 20, 30, 40)
print(type(tuple2))

# 打印元组
print(tuple2)
# 遍历元组
for i in tuple2:
    print(i)
# 通过索引访问元组的元素
print(tuple2[0])
print(tuple2[3])


# 合并或拼接
str1 = 'hello '
str2 = 'Python!'
print(str1 + str2)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list1 + list2)

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
print(tuple1 + tuple2)

# 复制
print(str1 * 10)
print(list1 * 10)
print(tuple1 * 10)

# 是否in
str3 = 'hello python! hello bigdata'
if 'bigdata' in str3:
    print('exists')
else:
    print('not exists')

# 求数据容器长度
print(len(str3))
print(len(list1))
print(len(tuple1))

# 手动输入三个数
num1 = int(input('请输入第一个数:'))
num2 = int(input('请输入第二个数:'))
num3 = int(input('请输入第三个数:'))
# 求三个数的最值
list3 = [num1, num2, num3]
max_num = max(list3)
min_num = min(list3)
print(f'max = {max_num},min = {min_num}')

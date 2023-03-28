# 查询方法，in
black_ip = ['192.168.89.77', '222.246.129.81', '172.16.54.33']
if '192.168.89.77' in black_ip:
    print('IP被锁定，禁止访问')
else:
    print('正常访问')

# 字符串中的in方法
str1 = 'hello python'
if 'py' in str1:
    print('py在str1中')
else:
    print('py不在str1中')

# 添加元素进列表 append
list1 = ['刘备', '曹操']
print(list1.append('孙权'))  # 不返回任何元素
print(list1)

# 合并列表 +
list2 = ['Tom', 'Lily']
list3 = ['Connor', 'Jony']
print(list2 + list3)

# 删除列表中的元素，remove
print(list1.remove('曹操'))  # 不返回任何元素
print(list1)

# 修改元素
list1[1] = '曹孟德'
print(list1)

# 翻转和排序
# reverse翻转，用切片也可以实现
list4 = ['5', '3', '2', '1', '7', '9']
list5 = ['刘备', '关羽', '张飞']

list5.reverse()
print(list5)
print(list5[::-1])

list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)

# 定义空字典
person = {}
# 添加数据
person['name'] = 'Tom'
person['gender'] = 'male'
person['age'] = 20
print(person)
# 修改数据
person['name'] = 'Lily'
person['gender'] = 'female'
print(person)
# 定义一个有数据的字典，'Connor', 'male', 25, 80
student = {'name': 'Connor', 'gender': 'male', 'age': 25, 'weight': 80}
# 删除键值对
del student['weight']
print(student)

# 定义student = {'name':'Jack', 'age':20, 'address':'广州市天河区'}
student = {'name': 'Jack', 'age': 20, 'address': '广州市天河区'}
# 获取字典中某个元素，打印字典
print(student['address'])
# 遍历字典
for i in student:
    print(i)
# 使用keys()方法获取键值，等价于遍历
for key in student.keys():
    print(key)
# 获取所有的value值，values
for value in student.values():
    print(value)
# 获取所有键值对，items
for item in student.items():
    print(item)

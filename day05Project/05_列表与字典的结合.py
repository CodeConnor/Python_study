# 开发一个学生管理系统
# 1、定义一个大列表，里面用于保存多个同学的信息
students = []
# 2、定义一个字典，保存同学信息
student = {'name': 'Tom', 'gender': 'male', 'age': 20}
# 3、将字典嵌套在列表中
students.append(student)
print(students)
# 4、多添加几个字典
student1 = {'name': 'Lily', 'gender': 'female', 'age': 21}
student2 = {'name': 'Connor', 'gender': 'female', 'age': 22}
students.append(student1)
students.append(student2)
print(students)
# 5、提示用户输入需要删除的同学信息
del_name = input('请输入需要删除的同学姓名：')
# 6、通过遍历，删除存储该同学信息的字典
for i in students:
    if i['name'] == del_name:
        students.remove(i)
        print('删除成功')
        break
else:
    print('未找到该同学')
print(students)

# students = [{'name': 'Lihua', 'age': 20, 'gender': 'male'},
#             {'name': 'Connor', 'age': 23, 'gender': 'male'},
#             {'name': 'Liying', 'age': 18, 'gender': 'female'}]
students = []

# global students
f = open('students.txt', 'w', encoding='utf-8')
if not students:
    print('【暂无数据需要保存！】')
else:

    f.write(str(students))
    print('【数据保存成功！】')
f.close()

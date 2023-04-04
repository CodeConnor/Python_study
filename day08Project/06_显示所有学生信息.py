students = [{'name': 'Lihua', 'age': 20, 'gender': 'male'},
            {'name': 'Connor', 'age': 23, 'gender': 'male'},
            {'name': 'Lily', 'age': 18, 'gender': 'female'}]

if not students:
    print('【暂无学生信息！】')
else:
    for i in students:
        print(f'姓名：{i["name"]}, 年龄：{i["age"]}, 性别：{i["gender"]}')

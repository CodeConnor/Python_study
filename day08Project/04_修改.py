students = [{'name': 'Lihua', 'age': 20, 'gender': 'male'},
            {'name': 'Connor', 'age': 23, 'gender': 'male'},
            {'name': 'Lily', 'age': 18, 'gender': 'female'}]

while True:
    # global students
    alter_name = input('请输入所要修改的学生姓名：')
    for i in students:
        if i['name'] == alter_name:
            # 提示输入修改信息
            name = input('请输入学生姓名：')
            age = int(input('请输入学生年龄：'))
            gender = input('请输入学性别：')
            # 修改students列表内的字典
            i['name'] = name
            i['age'] = age
            i['gender'] = gender
            print(f'【{alter_name}】信息已成功修改！')
            print(students)
            break
    # 遍历完成后，没查询到（没有break）时进行提示
    else:
        print('很抱歉，查询不到该学生！')

    user_cmd = input('【输入任意键继续】\n【输入q或者Q退出】\n:')
    # 判断退出或继续
    if user_cmd == 'q' or user_cmd == 'Q':
        break

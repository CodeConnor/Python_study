students = [{'name': 'Lihua', 'age': 20, 'gender': 'male'},
            {'name': 'Connor', 'age': 23, 'gender': 'male'},
            {'name': 'Lily', 'age': 18, 'gender': 'female'}]

while True:
    # global students
    select_name = input('请输入所要查询的学生姓名：')
    for i in students:
        if i['name'] == select_name:
            print(i)
            break
    else:
        print('很抱歉，查询不到该学生！')

    user_cmd = input('【输入任意键继续】\n【输入q或者Q退出】\n:')
    # 判断退出或继续
    if user_cmd == 'q' or user_cmd == 'Q':
        break
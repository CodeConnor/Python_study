students = [{'name': 'Lihua', 'age': 20, 'gender': 'male'},
            {'name': 'Connor', 'age': 23, 'gender': 'male'},
            {'name': 'Lily', 'age': 18, 'gender': 'female'}]

while True:
    del_name = input('请输入所要删除的学生姓名：')
    # 遍历学生列表
    for i in students:
        # 判断学生姓名是否存在
        if i['name'] == del_name:
            students.remove(i)
            print(f'【{del_name}】信息已成功删除！')
            break
    # 遍历完成后，没查询到（没有break）时进行提示
    else:
        print('【很抱歉，查询不到该学生！】')

    user_cmd = input('【输入任意键继续】\n【输入q或者Q退出】\n:')
    # 判断退出或继续
    if user_cmd == 'q' or user_cmd == 'Q':
        break
    print(students)
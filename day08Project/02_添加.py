# 添加同学信息
students = []

while True:
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    gender = input('请输入学性别：')
    # 将信息存入字典和列表
    student = {}
    student['name'] = name
    student['age'] = age
    student['gender'] = gender
    students.append(student)
    print(student)
    print(students)

    user_cmd = input('【输入任意键继续】\n【输入q或者Q退出】\n:')
    # 判断退出或继续
    if user_cmd == 'q' or user_cmd == 'Q':
        break


# 定义列表存储学生信息
students = []


# 定义menu函数，实现对系统功能界面的输出
def menu():
    print('-' * 40)
    print('            学生管理系统v1.0')
    print('【1】添加学生信息')
    print('【2】删除学生信息')
    print('【3】修改学生信息')
    print('【4】查询学生信息')
    print('【5】显示所有学生信息')
    print('【6】保存数据到系统')
    print('【7】加载数据到系统')
    print('【8】退出系统')
    print('-' * 40)


# 定义is_digit函数，判断用户是否输入数字
def is_digit(user_str):
    try:
        num = int(user_str)
        return num
    except:
        return


# 定义add_stu函数，实现添加学生信息
def add_stu():
    while True:
        user_cmd = input('--输入任意键继续--\n--输入q或者Q退出--\n:')
        # 判断退出或继续
        if user_cmd == 'q' or user_cmd == 'Q':
            break
        else:
            global students
            name = input('请输入学生姓名：')
            age = int(input('请输入学生年龄：'))
            gender = input('请输入学生性别：')
            # 将信息存入字典和列表
            student = {}
            student['name'] = name
            student['age'] = age
            student['gender'] = gender
            students.append(student)


# 定义del_stu函数，实现删除学生信息
def del_stu():
    while True:
        user_cmd = input('--输入任意键继续--\n--输入q或者Q退出--\n:')
        # 判断退出或继续
        if user_cmd == 'q' or user_cmd == 'Q':
            break
        else:
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
                print('很抱歉，查询不到该学生！')


# 定义alter_stu函数，实现修改学生信息
def alter_stu():
    while True:
        user_cmd = input('--输入任意键继续--\n--输入q或者Q退出--\n:')
        # 判断退出或继续
        if user_cmd == 'q' or user_cmd == 'Q':
            break
        else:
            global students
            alter_name = input('请输入所要修改的学生姓名：')
            for i in students:
                if i['name'] == alter_name:
                    # 提示输入修改信息
                    name = input('请输入新学生姓名：')
                    age = int(input('请输入新学生年龄：'))
                    gender = input('请输入新学生性别：')
                    # 修改students列表内的字典
                    i['name'] = name
                    i['age'] = age
                    i['gender'] = gender
                    print(f'【{alter_name}】信息已成功修改！')
                    break
            # 遍历完成后，没查询到（没有break）时进行提示
            else:
                print('很抱歉，查询不到该学生！')


# 系统的调用
while True:
    menu()
    user_str = input('请按照提示输入数字：')
    # 判断输入内容是否是数字
    user_num = is_digit(user_str)

    if user_num == 1:
        add_stu()
    elif user_num == 2:
        del_stu()
    elif user_num == 3:
        alter_stu()
    elif user_num == 4:
        pass
    elif user_num == 5:
        pass
    elif user_num == 6:
        pass
    elif user_num == 7:
        pass

    # 退出系统
    elif user_num == 8:
        print('已成功退出系统，欢迎下次使用！')
        break

    # 当用户输入错内容时，返回功能提示菜单
    else:
        print('输入错误，请按提示输入正确内容！')

students = [{'name': 'Lihua', 'age': 20, 'gender': 'male'},
            {'name': 'Connor', 'age': 23, 'gender': 'male'},
            {'name': 'Lily', 'age': 18, 'gender': 'female'}]

while True:
    user_cmd = input('--输入任意键继续--\n--输入q或者Q退出--\n:')
    # 判断退出或继续
    if user_cmd == 'q' or user_cmd == 'Q':
        break
    else:

# 案例：用for循环实现用户登录
# ①输入用户名和密码
# ②判断用户名和密码是否正确
# ③登录仅有三次机会，超过3次会报错
# ④如果用户登录失败，则提示用户名错误还是密码错误
# ⑤获取剩余的登录次数
name = 'admin'
key = 'admin1234'
count = 0
for i in range(3):
    username = input('账号：')
    password = input('密码：')
    if username == name:
        if password == key:
            print('登录成功')
            break
        else:
            print('密码错误，请重新输入')
            count += 1
            print(f'错误次数剩余{3-count}次')
    else:
        print('账号错误，请重新输入')
        count += 1
        print(f'错误次数剩余{3 - count}次')
else:
    print('登录错误次数过多，请等待10分钟')
# 使用while循环计算1~100的累加和（包含1和100）
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f'sum = {sum}')

'''
使用while循环打印如下图形
*
* *
* * *
* * * *
* * * * * 
'''
i = 1
while i <= 5:
    print('* ' * i)
    i += 1

# 编写代码模拟用户登陆。要求：用户名为 python，密码 123456
# 如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入
sys_name = 'python'
sys_pwd = '123456'
while True:
    user_name = input('请输入用户名：')
    user_pwd = input('请输入密码：')
    if user_name == sys_name and user_pwd == sys_pwd:
        print('欢迎光临')
        break
    else:
        print('用户名或密码错误，请重新登录')

# 设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字
# 如果遇见7和7的倍数则打印“过！”跳过本次循环。
# 使用continue
i = 1
while i <= 100:
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        print('过！')
        i += 1
        continue
    print(f'i = {i}')
    i += 1

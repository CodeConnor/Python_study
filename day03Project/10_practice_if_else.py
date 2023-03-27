# 坐公交：假设坐公交需要买票上车，书写程序要求如下：
# 1. 如果有票则可以上车，否则不能上车
# 2. 上车后，如果有座位可以坐下，否则不能坐下。已有程序如下，请补全程序：

# ticket取值为1表示有票，取值为0表示无票
ticket = 1
# seat取值为1表示有座，取值为0表示无座
seat = 1
if ticket == 1:
    print('允许上车')
    if seat == 1:
        print('可以落座')
    else:
        print('无法落座')
else:
    print('无法上车')

# 用户登录输入验证码，已知验证码是`axyz`,  验证码正确可以登录，否则输出：验证码错误。
code = input('请输入验证码：')
if code == 'axyz':
    print('验证码正确')
else:
    print('验证码错误')

# 制作用户登录系统：已知A用户注册的用户名为`aaa`，密码是`123456`。具体要求如下：
# 登录时需要验证用户名、密码、验证码(固定验证码为`qwer`)。
# 提示：系统先验证验证码是否正确，正确后再验证用户名和密码。

# 系统内用户名、密码、验证码数据
sys_name = 'aaa'
sys_pwd = '123456'
sys_code = 'qwer'

# 用户输入用户名、密码、验证码
user_name = input('请输入用户名：')
user_pwd = input('请输入密码：')
user_code = input('请输入验证码：')

if user_code == sys_code:
    print('验证码正确')
    if user_name == sys_name and user_pwd == sys_pwd:
        print('恭喜您，登录成功')
    else:
        print('用户名或密码错误，请重新输入')
else:
    print('验证码错误，请重新输入')

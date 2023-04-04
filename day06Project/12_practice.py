# ------------------------------------------------------------1
# 定义一个简单的函数run，
# 函数的功能是输出"我在跑步" 以及 “管住嘴，迈开腿”，并调用此函数。
def run():
    print('我在跑步\n管住嘴，迈开腿')


run()

# ------------------------------------------------------------2
# 在第一题中，我们已经用函数run实现了一些功能，
# 如果我们想run函数做的操作执行1000遍，怎么实现代码？
i = 1
while i <= 1000:
    run()
    i += 1


# ------------------------------------------------------------3
# 现在我们来实现一个有参数有返回值的函数addnum，并实现调用，要求如下 ：
# 我们要用函数来实现7与13两个数字的加法运算，并返回两个数的和进行输出
def addnum(num1, num2):
    result = num1 + num2
    return result


print(addnum(7, 13))


# ------------------------------------------------------------4
# 在填写个人资料时，如果选了女性，那么性别是女；
# 如果不选性别，那就是默认是男，那么这个功能用函数怎么实现？
# 要求如下：定义一个函数gender，并在函数中将“所选性别为*”，并可以成功调用运行。
def gender(a='男'):
    print(f'所选性别为：{a}')


gender()
gender('女')


# ------------------------------------------------------------5
# 要求实现一段代码：
# 声明一个函数num1，并且在调用函数的时候，
# 不管输入多少个非关键字参数，函数都可以运行，
# 且在函数内部还要把每个参数输出到屏幕上。
def num1(*args):
    for i in args:
        print(i)


num1(1, 2, 3)


# ------------------------------------------------------------6
# 如下所示这是一个字典，{"name":"电脑","price":7000}
# 请定义这样一个函数num2，讲上述字典中的键值对传入到函数num中
# 要求用不定长参数来接收，并在函数中打印键值对输出
# 输出格式为：key：name   value：电脑
#           key：price    value：7000
def num2(**kwargs):
    for key, value in kwargs.items():
        print(f'key:{key}  value:{value}')


dict1 = {"name": "电脑", "price": 7000}
for key, value in dict1.items():
    num2(key=value)


# ------------------------------------------------------------7
# 对于一个函数num3，当调用num3(1,2,a=3,b=4)
# 和调用num3(3,4,5,6,a=1)以及num3(a=1,b=2)的时候都可以正常运行，
# 并且可以对元组以及字典类型进行遍历输出，
# 对字典类型进行输出字典的键值对(形式为：key：a，value：1)，
# 请写出这个函数并完成调用。
def num3(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(f'key:{key}  value:{value}')


num3(1, 2, a=3, b=4)
num3(3, 4, 5, 6, a=1)
num3(a=1, b=2)
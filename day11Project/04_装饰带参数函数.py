# -----------------------案例：新增输出日志--------------------------------------
# 需求：在输出结果之前，添加一个打印日志的功能 => print('-----日志信息；正在进行计算-----')

# 源函数
def sum_num(num1, num2):
    result = num1 + num2
    print(f'sum = {result}')


sum_num(10, 30)


# -----------------------案例：装饰不定长参数函数--------------------------------------
# 增加输出日志功能


# 源函数
def sum_args(*args, **kwargs):
    result = 0
    # 遍历参数，并求和
    for i in args:  # 遍历元组
        result += i
    for value in kwargs.values():  # 取字典的值
        result += value
    print(f'sum = {result}')


sum_args(10, 20, 30, a=40, b=50)
# 以下功能使用函数实现
# 返回值有两个
def func1():
    return 1
    return 2


result1 = func1()  # 只会返回第一个return的结果
print(result1)


# 返回一个元组
def func2():
    return 1, 2, 3  # 返回多个值时，会返回元组类型


result2 = func2()
print(result2)


# 没有返回值
def func3():
    pass  # 定义一个空函数


print(func3)


# 返回两个数的加减乘除结果，写函数说明文档
def calculate(num1, num2):
    '''
    该函数用于计算两个数分别进行加减乘除的值
    :param num1: int, 第一个参数
    :param num2: int, 第二个参数
    :return: 分别返回两者加减乘除的值，（加，减，乘，除）
    '''
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2
    return add, subtract, multiply, divide


result3 = calculate(20, 5)
print(result3)
# 查看指定函数的说明文档
help(calculate)


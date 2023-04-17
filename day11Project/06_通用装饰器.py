# 定义一个通用装饰器，用于打印日志信息


# 源函数
def sub_nums(num1, num2):
    result = num1 - num2
    return result


print(f'sub = {sub_nums(20, 10)}')

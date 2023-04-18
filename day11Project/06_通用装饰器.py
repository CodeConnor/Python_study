# 定义一个通用装饰器，用于打印日志信息
def logging(fn):
    def inner(*args, **kwargs):
        print('-----日志信息；正在进行计算-----')
        return fn(*args, **kwargs)
    return inner

# 源函数
@logging
def sub_nums(num1, num2):
    result = num1 - num2
    return result

print(f'sub = {sub_nums(20, 10)}')

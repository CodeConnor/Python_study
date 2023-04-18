# 分别对sum和sub函数输出不同的日志
def decoration(flag):
    def logging(fn):
        def inner(*args, **kwargs):
            if flag == '+':
                print('-----日志信息；正在进行加法计算-----')
            elif flag == '-':
                print('-----日志信息；正在进行减法计算-----')
            return fn(*args, **kwargs)
        return inner
    return logging

# 源函数
@decoration('+')
def sum_nums(num1, num2):
    result = num1 + num2
    return result

print(f'sum = {sum_nums(20, 10)}')

@decoration('-')
def sub_nums(num1, num2):
    result = num1 - num2
    return result

print(f'sub = {sub_nums(20, 10)}')

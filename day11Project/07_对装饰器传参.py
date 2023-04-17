# 分别对sum和sub函数输出不同的日志


# 源函数
@logging('+')
def sum_nums(num1, num2):
    result = num1 + num2
    return result


print(f'sum = {sum_nums(20, 10)}')


@logging('-')
def sub_nums(num1, num2):
    result = num1 - num2
    return result


print(f'sub = {sub_nums(20, 10)}')

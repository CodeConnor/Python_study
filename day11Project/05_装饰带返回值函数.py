# -----------------------案例：装饰带返回值的函数-------------------------------------
# 新增日志信息


# 源函数
def sum_num(num1, num2):
    result = num1 + num2
    return result


print(f'sum = {sum_num(10, 20)}')

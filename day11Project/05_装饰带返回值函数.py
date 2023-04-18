# -----------------------案例：装饰带返回值的函数-------------------------------------
# 新增日志信息
def logging(fn):
    def inner(*args, **kwargs):
        print('-----日志信息；正在进行计算-----')
        return fn(*args, **kwargs)
    return inner

# 源函数
@logging
def sum_num(num1, num2):
    result = num1 + num2
    return result

print(f'sum = {sum_num(10, 20)}')

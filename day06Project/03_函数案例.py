# 求三个数平均值
def avg_func(num1, num2, num3):
    '''
    该函数用于求三个数的平均值
    :param num1: int，参数1
    :param num2: int，参数2
    :param num3: int，参数3
    :return: 返回三个数的平均值avg
    '''
    avg = (num1 + num2 + num3) / 3
    return avg


num1 = int(input('请输入第1个数：'))
num2 = int(input('请输入第2个数：'))
num3 = int(input('请输入第3个数：'))
result1 = avg_func(num1, num2, num3)
print(result1)


# 编写一个函数,有一个参数str1,输入信息如'1.2.3.4.5',使用函数对其进行处理,要求最终的返回结果为'5-4-3-2-1'
def str_func(str1):
    '''
    将输入字符串先翻转，然后将’.‘替换为’-‘
    :param str1: str，参数1
    :return: 返回处理后字符串
    '''
    str2 = str1[::-1]  # 翻转字符串
    result = str2.replace('.', '-')  # 替换
    return result


result2 = str_func('1.2.3.4.5')
print(result2)


# 生成4位数的验证码
import random
def code_func():
    '''
    用于随机生成4位验证码
    :return: 返回4位的验证码
    '''
    str1 = '23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'  # 验证码的范围
    code = ''  # 定义空容器存储验证码
    i = 1
    while i <= 4:  # 生成4位，即循环4次
        index = random.randint(0, len(str1) - 1)  # 求出字符串中的随机一个索引
        code += str1[index]  # 按照索引，切片1个字符
        i += 1
    return code


result3 = code_func()
print(f'验证码为：{result3}')

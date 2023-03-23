# 案例：求两个数中的最大值

import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# if else结构
# if num1 > num2:
#     maxnum = num1
# else:
#     maxnum = num2

# 三目运算符
maxnum = num1 if num1 > num2 else num2
print(f'num1 = {num1}, num2 = {num2}, maxnum = {maxnum}')

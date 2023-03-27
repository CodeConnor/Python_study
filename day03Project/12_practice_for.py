# 请用户输入一个数，使用for计算是否为素数
num1 = int(input('请输入一个数：'))
if num1 <= 0:
    print('不是素数')
else:
    for i in range(2, num1, 1):
        if num1 % i == 0:
            print('不是素数')
            break
    else:
        print('是素数')

# 要求用户输入一个字符串，遍历当前字符串并打印，
# 如果遇见“q”,则跳出循环。如果遇见“ ”（空格）则跳过当前输出。
str1 = input('请输入字符串：')
for i in str1:
    if i == 'q':
        break
    elif i == ' ':
        continue
    print(i)

# 使用for循环计算数值1到用户输入数值的累加和
num2 = int(input('请输入数字：'))
sum = 0
if num2 <= 0:
    for i in range(num2, 2, 1):
        sum += i
    print(f'从1到{num2}的累加值为{sum}')
else:
    for i in range(1, num2 + 1, 1):
        sum += i
    print(f'从1到{num2}的累加值为{sum}')

# 分别使用for循环和while循环，求100~200的所有素数
for i1 in range(100, 201, 1):
    for i2 in range(2, i1, 1):
        if i1 % i2 == 0:
            break
    else:
        print(f'{i1}是素数')

i = 100
while i <= 200:
    divisor = 2
    while divisor < i:
        if i % divisor == 0:
            break
        divisor += 1
    else:
        print(f'{i}是素数')
    i += 1


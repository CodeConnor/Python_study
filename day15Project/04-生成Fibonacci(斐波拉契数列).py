# 数列中第一个数为1，第二个数为1，其后的每一个数都可由前两个数相加得到
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# 迭代
def fibonacci1(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_prev = 0
    fib_curr = 1
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    return fib_curr


print(fibonacci1(10))  # 输出第10个斐波那契数：55


# 递归
def fibonacci2(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci2(n - 1) + fibonacci2(n - 2)


print(fibonacci2(10))  # 输出第10个斐波那契数：55

# 生成器
def fib_generator(max):
    n = 1  # 循环次数
    a, b = 0, 1  # 数列的相邻两位数字
    while n <= max:
        a, b = b, a+b
        yield a
        n += 1

fib = fib_generator(10)
for i in fib:
    print(i)
# 遍历字符串，打印每个字母
for i in str('xiaobang'):
    print(i)

# 使用for循环求1-100的和，range方法
sum = 0
for i in range(1, 101, 1):  # range中结束值要选101，不包括101
    sum += i
print(sum)

# 使用for循环求1-100中的偶数和
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)
# 或者
sum = 0
for i in range(101):  # stop值是101，默认start和step都是1
    if i % 2 == 0:
        sum += i
print(sum)
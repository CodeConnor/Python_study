# 例1：循环打印1-5
i = 1
while i <= 5:
    print(i)
    i += 1

# 例2：求1-100的和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# 例3：求1-100中偶数的和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:  # 取余筛选偶数
        sum += i
    i += 1
print(sum)

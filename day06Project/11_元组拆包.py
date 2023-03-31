tuple1 = (10, 20, 30)
# 拆包
num1, num2, num3 = tuple1

# 以上代码可以简写为
num1, num2, num3 = (10, 20, 30)
# 还可简写为
num1, num2, num3 = 10, 20, 30
print(num1, num2, num3)

# 案例：实现两个变量的交换
c1 = 'cola'
c2 = 'milk'

c2, c1 = c1, c2
print(c1)
print(c2)

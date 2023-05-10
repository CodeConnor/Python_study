# 目的: 当x*y = 64的时候退出循环
x = 1
while x < 10:
    y = 1
    while y < 10:
        if x * y == 64:
            break
        y += 1
    if x * y == 64:
        break
    x += 1
print(x, y)

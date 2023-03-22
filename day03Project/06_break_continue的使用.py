# 吃5个苹果案例
# break 吃到第四个吃饱了
i = 1
while i <= 5:
    if i == 4:
        print('吃饱了不吃了')
        break  # 终止整个循环
    print(f'正在吃第{i}个苹果')
    i += 1

# continue 第3个苹果坏了，跳过第三个，接着吃完苹果
i = 1
while i <= 5:
    if i == 3:
        print('这个苹果坏了，不吃')
        i += 1  # 不增加计数器的值就会死循环
        continue  # 跳出第三次循环开始第四次
    print(f'正在吃第{i}个苹果')
    i += 1
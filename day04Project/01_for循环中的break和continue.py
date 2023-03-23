# 打印字符串内容，遇到字符b就终止整个循环
str1 = 'xiaobang'
for i in str1:
    if i == 'b':
        print('break')
        break
    print(i)

# 打印字符串内容，遇到字符b就跳过当前循环执行下个循环
str1 = 'xiaobang'
for i in str1:
    if i == 'b':
        print('continue')
        continue
    print(i)

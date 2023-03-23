# 打印字符串xiaobang并正常执行else后的代码
str1 = 'xiaobang'
for i in str1:
    print(i)
else:
    print('打印成功')
# 遇到break时
for i in str1:
    if i == 'b':
        break
    print(i)
else:
    print('打印成功')

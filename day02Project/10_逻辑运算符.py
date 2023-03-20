# 短路运算
print(3 and 4 and 5)  # T T 7
print(5 and 6 or 7)  # T T 6
4 > 3 and print('hello world')  # T str


print(5 or 6 and 7) # 先执行and，结果为7，再执行5 or 7，结果是5
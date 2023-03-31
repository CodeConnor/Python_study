# ------------------------------------------------------------1
# 在当前目录先，创建movie.txt文件，文件内容是：
# 功夫，周星驰
# 一出好戏，黄渤
# 我不是药神，徐峥
# 分两步读写，第一步先用写入模式打开文件
f = open('movie.txt', 'w', encoding='utf-8')

f.write('''
功夫，周星驰
一出好戏，黄渤
我不是药神，徐峥
''')
f.close()
# 再用只读模式打开文件
f = open('movie.txt', 'r', encoding='utf-8')
content = f.read()
print(content)
f.close()

# 使用读写模式打开文件
f = open('movie.txt', 'r+', encoding='utf-8')
f.write('''功夫，周星驰
一出好戏，黄渤
我不是药神，徐峥
''')
# 我们使用了 seek(0) 方法将文件指针重置到文件开头，以便我们可以读取刚刚写入的内容。
# 如果没有调用 seek(0) 方法，读取操作将会返回一个空字符串，因为文件指针已经位于文件末尾。
f.seek(0)
content = f.read()
print(content)
f.close()

# ------------------------------------------------------------2
# 将第一题创建好的文件打开，并读取内容
# 一次全部读取
# 每次读取一行
f = open('movie.txt', 'r', encoding='utf-8')
a = f.read()
f.seek(0)  # 每次读取完全部内容指针都会到末行，需要重置
b = f.readlines()
f.seek(0)
c = f.readline()
print(a)
print(b)
print(c)
f.close()

# ------------------------------------------------------------3


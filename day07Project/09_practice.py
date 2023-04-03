# ------------------------------------------------------------1
# 在当前目录先，创建movie.txt文件，文件内容是：
# 功夫，周星驰
# 一出好戏，黄渤
# 我不是药神，徐峥
# 分两步读写，第一步先用写入模式打开文件
f = open('movie.txt', 'w', encoding='utf-8')

f.write('''功夫，周星驰
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
# 使用os模块创建一个名为“hello”的文件夹
import os
if not os.path.exists('hello'):
    os.mkdir('hello')
# 获取文件夹当前所在目录
print(os.getcwd())
# 获取当前的目录列表
print(os.listdir())
# 改变文件的操作路径
os.chdir('hello')
print(os.getcwd())
# 将hello文件夹删除
os.chdir('..')
os.rmdir('hello')

# ------------------------------------------------------------4
# 提示用户输入文件名。例：film.txt
name = input('请输入文件名：')
os.remove(name)
# 创建用户输入的名字的文件
f = open(name, 'w+', encoding='utf-8')
# 打开文件写入如下信息
# 功夫，周星驰
# 一出好戏，黄渤
# 我不是药神，徐峥
f.write('''功夫，周星驰
一出好戏，黄渤
我不是药神，徐峥
''')
f.seek(0)
# 将输入的数据输出到终端上
content = f.read()
print(content)
# 在文件夹中创建film副本.txt文件
index = name.rfind('.')
filename = name[:index]
postfix = name[index:]
copy_file = filename + '副本' + postfix
os.remove(copy_file)
copy_f = open(copy_file, 'w+', encoding='utf-8')
# 将film.txt文件中的数据写入film副本.txt文件中
copy_f.write(content)
copy_f.seek(0)
# 打开文件，查看文件中内容
copy_content = copy_f.read()
print(copy_content)
f.close()
copy_f.close()

# ------------------------------------------------------------5
# 创建一个名字py文件夹
# 进入py文件夹中创建5个文件，
# 文件名分别为python-1.txt，python-2.txt，python-3.txt，python-4.txt，python-5.txt
# 然后将py文件夹中的所有文件都改名为
# [hello]python-1.txt，[hello]python-2.txt，[hello]python-3.txt，[hello]python-4.txt，[hello]python-5.txt
import os
if not os.path.exists('py'):
    os.mkdir('py')
os.chdir('py')
filename = 'python-'
prefix = '[hello]'
postfix = '.txt'
# 创建文件
i = 1
while i <= 5:
    file = filename + str(i) + postfix
    if not os.path.exists(file):
        with open(file, 'w') as f:  # 使用with打开文件之后会自动关闭
            pass
    i += 1
print(os.listdir())
# 文件改名
i = 1
while i <= 5:
    file = filename + str(i) + postfix
    if os.path.exists(file):
        os.rename(file, prefix + file)
    i += 1
print(os.listdir())

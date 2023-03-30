# read(size)方法
# r模式，打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 读取文件内容
# content = f.read()  # 读取文件所有内容
content = f.read(1)  # 只读取一个字符
print(content)

# 关闭文件
f.close()

# readlines方法
f = open('python.txt', 'r', encoding='utf-8')
# 读取文件内容
content = f.readlines()
print(content)
# 关闭文件
f.close()


# readline方法
f = open('python.txt', 'r', encoding='utf-8')
# 使用循环实现一次执行读取多行
while True:
    content = f.readline()
    if not content:  # 当文件内容读取完后继续读会产生空内容，判断是否为空即可中断循环
        break
    print(content, end='')  # 解决每print一次就会出现一次空行的问题
# 关闭文件
f.close()


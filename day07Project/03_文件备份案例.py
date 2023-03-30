# 需求：用户输入当前目录下任意文件名，完成对该文件的备份功能(备份文件名为xx[备份]后缀，例如：(test[备份].txt)。
# ①命名变化:test.txt => 备份 => test[备份].txt
# ②内容变化:需要把旧文件中的内容完全拷贝到新文件中
# rfind()方法,从左向右查找,返回这个关键词在最后一次出现的位置
oldname = input('请输入您要备份的文件名称:')
index = oldname.rfind('.')
filename = oldname[:index]
postfix = oldname[index:]
newname = filename + '[备份]' + postfix
# 打开旧文件，创建新文件
old_f = open(oldname, 'rb')
new_f = open(newname, 'wb')
# 读取文件，写入内容
while True:
    content = old_f.read(1024)  # r模式size代表字符长度,rb模式size代表字节大小 => 1KB
    if not content:
        break
    new_f.write(content)

old_f.close()
new_f.close()

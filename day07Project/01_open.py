# 使用python.txt举例
# 打开文件，使用utf-8编码保存(要不中文会乱码)
f = open('python.txt', 'w', encoding='utf-8')
# 写入内容
f.write('''
Life is short, I study Python!
人生苦短，我学Python！
''')
# 关闭文件，节省计算机资源
f.close()

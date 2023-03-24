# 定义一个字符串
str1 = 'hello world hello linux hello python'
# 查找linux子串是否出现在字符串中
print(type(str1.find('linux')))  # 返回int18，即linux开始的索引
print(str1.find('linux'))
# 在str1中查找不存在的子串
print(str1.find('aaaaaaa'))  # 返回-1，不存在该子串

file = input('请输入您要上传文件的名称：')  # 假如输入avatar.png
# 获取点号的索引下标
index = file.find('.')
print(index)
# 求文件名称filename
filename = file[:index]
print(filename)
# 求文件后缀postfix
postfix = file[index + 1:]
print(postfix)

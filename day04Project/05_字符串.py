str1 = '这是一行字符串'
print(str1)
print(type(str1))

# 换行
str2 = '''
	这是
	很多行
	字符串
'''
print(str2)
print(type(str2))

# 定义特殊字符串，例如：I'm Connor.
# 字符串中若包含引号，可以使用以下方法来定义：
# ①交叉定义，比如里面是单引号，外面就使用双引号
# ②使用反斜杠\转义字符，对引号进行转义
print("I'm Connor")
print('I\'m Connor')

# 通过索引输出字符串的字符
str3 = 'xiaobang'
print(str3[0])
print(str3[1])
print(str3[2])
# ---------------------------------------------------------eg.1
# 查找字符串中是否包含数字"8"
# 1、导入模块
import re
# 2、匹配结果
str1 = '13086062869'
result = re.findall('8', str1)  # 返回1个列表
print(result)

# ---------------------------------------------------------eg.2
# 查找字符串中是否包含任意数字
str2 = 'abcd6efgh'
result = re.findall('\d', str2)  # \d 代表数字
print(result)

# ---------------------------------------------------------eg.3
# 查找字符串中所有非数字字符
str3 = 'sbcd234aa@#$%^&*'
result = re.findall('\D', str3)  # \D 代表非数字
print(result)

# ---------------------------------------------------------eg.4
# 匹配字符串中开头字符
str4 = 'wxxxx'
result = re.match('.', str4)  # 返回1个对象
print(result.group())  # 使用group提取结果

result = re.match('[a-z]', str4)  # 查小写字母
print(result.group())

result = re.match('[^0-9]', str4)  # 等价于\D，查非数字
print(result.group())

str5 = '  aa  bb'
result = re.match('\s', str5)  # 查空白
print(result.group())
print(result)

# ---------------------------------------------------------eg.5
# 匹配字符串中特殊与非特殊字符
str6 = " ,.<>/?:;'[]{}\|-_=+!@#$%^&*()~`aA1你"
result = re.findall('\w', str6)
print(result)
result = re.findall('\W', str6)
print(result)
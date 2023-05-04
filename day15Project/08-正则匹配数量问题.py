import re

str1 = '123aabbcc'
# 匹配连续3位数字
result = re.match('\d{3}', str1)
print(result.group())

# 匹配所有任意字符
result = re.match('.*', str1)
print(result.group())

# 匹配1或者10
result = re.match('10?', str1)
print(result.group())

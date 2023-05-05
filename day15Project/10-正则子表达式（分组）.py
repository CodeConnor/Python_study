import re

str1 = 'abcdef123dhijklmn'
result = re.search(r'\d(\d)(\d)', str1)
print(result.group())  # 获取正则匹配的所有内容
print(result.group(1))  # 获取1号分组匹配到的内容
print(result.group(2))  # 获取2号分组匹配到的内容

# 使匹配结果为1212的形式
str2 = 'abcd121234345656efgh'
result2 = re.search(r'(\d)(\d)\1\2', str2)  # 只能匹配出第一个结果
print(result2.group())  # 1212

result3 = re.finditer(r'(\d)(\d)\1\2', str2)  # 可匹配出多个结果，结果需要遍历
for i in result3:
    print(i.group())  # 1212  3434  5656

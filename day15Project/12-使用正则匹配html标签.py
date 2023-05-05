# 匹配出<html><h1>www.aaa123ABC.com</h1></html>
import re

str1 = '<html><h1>www.aaa123ABC.com</h1></html>'
result = re.search(r'<(\w+)><(\w+)>(.*)</\2></\1>', str1)  # 成对标签可以使用反向引用匹配
if result:
    print(result.group())
    print(result.group(3))
else:
    print('No matching results')

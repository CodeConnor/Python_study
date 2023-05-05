import re

# 使用别名匹配邮箱
str1 = 'my email is abc@example.com'
result1 = re.search(r'my email is (?P<email>\w+@\w+\.com)', str1)  # \. 将.进行转译，使其不再代表任何字符而仅代表.

print(result1.group('email'))  # 只读取email
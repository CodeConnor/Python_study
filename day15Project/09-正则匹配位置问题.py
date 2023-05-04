import re

# 字符串保存11位手机号码，验证手机号码是否合理
mobile = '13079992999'
# 合理手机号：只有11位，以1开头，第2位不能是0、1、2，以数字结尾
result = re.match('^1[3456789]\d{9}$', mobile)
print(result)
if result:  # 如果不符合正则，返回空值，通过空值判断号码合理
    print('合理')
else:
    print('不合理')
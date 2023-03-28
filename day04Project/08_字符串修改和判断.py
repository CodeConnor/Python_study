str1 = 'hello linux and hello linux'
# 把字符串中所有linux字符替换为python
print(str1.replace('linux', 'python'))
# 把字符串中的第一个linux进行替换为python
print(str1.replace('linux', 'python', 1))  # 可指定替换哪一个子串，不指定就是替换全部
# 把and字符串替换为&&
print(str1.replace('and', '&&'))
# 字符串切割
str2 = 'apple-banana-orange'
print(str2.split('-'))  # 切割符号在后
# 序列拼接
list1 = ['apple', 'banana', 'orange']
print('-'.join(list1))  # 拼接符号在前

# 输入字符串并判断是否是纯数字，是则返回数字，反之返回error
user_input = input('请输入数字：')
if user_input.isdigit():
    print(user_input)
else:
    print('error，请输入数字')

# 如果需要使用变量保存以下字符串，我们该如何书写代码
# 鲁迅说:"我没有说过这句话"
str1 = '鲁迅说:"我没有说过这句话"'
print(str1)

# 做一个简单的用户信息管理系统：
# 提示用户依次输入姓名，年龄和爱好
# 并且在输入完成之后，一次性将用户输入的数据展示出来
# name = input('请输入姓名：')
# age = input('请输入年龄：')
# hobby = input('请输入爱好：')
# print(f'姓名：{name}  年龄：{age}  爱好：{hobby}')

# 现有字符串如下，请使用切片提取出ceg
words = "abcdefghi"
str2 = words[2:7:2]
print(str2)

# 现有：tuple1 = ("tom","kaisa","alisi","xiaoming","songshu")
# 我想获得“alisi”这个内容，你能否想到三种方法来做？
tuple1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
# ①
print(tuple1[2])
# ②
if "alisi" in tuple1:
    print("alisi")
# ③
for i in tuple1:
    if i == "alisi":
        print(i)

# 有如下元组：
# tuple1 = ("tom","kaisa","alisi","xiaoming","songshu")
# 求出他的长度
result = len(tuple1)
print(result)



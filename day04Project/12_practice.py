# ------------------------------------------------------------1
# 如果需要使用变量保存以下字符串，我们该如何书写代码
# 鲁迅说:"我没有说过这句话"
str1 = '鲁迅说:"我没有说过这句话"'
print(str1)

# ------------------------------------------------------------2
# 做一个简单的用户信息管理系统：
# 提示用户依次输入姓名，年龄和爱好
# 并且在输入完成之后，一次性将用户输入的数据展示出来
# name = input('请输入姓名：')
# age = input('请输入年龄：')
# hobby = input('请输入爱好：')
# print(f'姓名：{name}  年龄：{age}  爱好：{hobby}')

# ------------------------------------------------------------3
# 现有字符串如下，请使用切片提取出ceg
words = "abcdefghi"
str2 = words[2:7:2]
print(str2)

# ------------------------------------------------------------4
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

# ------------------------------------------------------------5
# 有如下元组：
# tuple1 = ("tom","kaisa","alisi","xiaoming","songshu")
# 求出他的长度
result = len(tuple1)
print(result)

# ------------------------------------------------------------6
# 需要在一个字符串'hello python'中查找python这个关键字，如何实现？
str3 = 'hello python'
print(str3.find('python'))

# ------------------------------------------------------------7
# 将下列两个列表合并，将合并后的列表去重，之后降序并输出
list1 = [11, 45, 34, 51, 90, 45]
list2 = [4, 16, 23, 0, 11]
# 转换成集合自动去重，再转换回列表排序输出
list0 = list(set(list2 + list1))
list0.sort(reverse=True)
print(list0)

# 使用遍历
list3 = []
# 遍历对比list3和list1之间有没有重复
for num1 in list1:
    for num3 in list3:
        if num1 == num3:
            break
    else:
        list3.append(num1)

for num2 in list2:
    for num3 in list3:
        if num2 == num3:
            break
    else:
        list3.append(num2)
list3.sort(reverse=True)
print(list3)

# ------------------------------------------------------------8
# 现有列表：
# namelist =["tom","kaisa","alisi",["xiaoming","songshu"]]
# 现在有个要求，将最外层的列表转换成元组存储，里面的小列表不变；
# 并且向小列表中添加一个元素“python”
namelist = ["tom", "kaisa", "alisi", ["xiaoming", "songshu"]]
nametuple = tuple(namelist)
nametuple[3].append('python')
print(nametuple)
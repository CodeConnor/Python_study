# 定义列表names
names = ['Tom', 'Lily', 'Lihua', 'Connor']
print(names)
print(type(names))

# 访问列表内元素
print(names[0])
print(names[3])
print(len(names))

# 遍历列表
i = 0
while i < len(names):
    print(names[i])
    i += 1

for i in names:
    print(i)

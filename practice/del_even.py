# 要求： 现有一个列表 li = [1,2,3,4,6,7,8,10,12],删除列表中的偶数数据
# 方法一，while循环
li = [1, 2, 3, 4, 6, 7, 8, 10, 12]
index = 0
while index < len(li):
    if li[index] % 2 == 0:
        del li[index]
        continue
    index += 1
print(li)

# 方法二，for循环
li = [1, 2, 3, 4, 6, 7, 8, 10, 12]
for i in li[:]:
    if i % 2 == 0:
        li.remove(i)
print(li)

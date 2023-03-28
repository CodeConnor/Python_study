# 定义一个空集合
set1 = set()
# 追加数据10,20,30,40,20,10
set1.add(10)
set1.add(20)
set1.add(30)
set1.add(40)
set1.add(20)
set1.add(10)
print(set1)
# 删除数据20
set1.remove(20)
print(set1)
# 随机删除某个元素
set1.pop()
print(set1)
# 判断元素是否出现在集合中
if 40 in set1:
    print('exists')
else:
    print('not exists')


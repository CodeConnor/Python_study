# 循环10000000次，每次循环添加一个元素进列表，求程序运行时间
from time import *  # 直接导入time的所有函数
start = time()  # 直接使用函数名获取当前时间，而不需要time.time()
# 开始循环
list1 = []
for i in range(10000000):
    list1.append(i)

end = time()
execution = end - start  # 计算程序执行时间
print(f'程序执行时间为：{execution}s')
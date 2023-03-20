# 定义变量
name = 'Connor'
age = 18
address = 'shanghai'

# 输出变量（普通输出）
print('我的名字是:', name, '我的年龄:', age, '我的地址:', address)
# 百分号格式化输出
print('我的名字是:%s, 我的年龄:%d, 我的地址:%s' % (name, age, address))
# 案例：定义两个变量title=大白菜，price=3.5.按照如下格式进行输出：今天蔬菜特价，大白菜只要3.5元／斤。
title = '大白菜'
price = 3.5
print('今天蔬菜特价，%s只要%.1f元/斤' % (title, price))
# 案例：定义两个变量id=1，name='Connor'，按照如下格式进行输出：姓名：Connor，学号：000001
id = 1
name = 'Connor'
print('姓名：%s，学号：%06d' % (name, id))
# 案例：由于受到俄罗斯与乌克兰战争影响，原油价格上浮5%！
num = 5
print('原油价格上浮%d%%' % num)

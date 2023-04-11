# 需求：统计这个类生成了多少个对象
# 定义Person类
class Person(object):
    # 定义类属性：计数器，统计对象创建个数
    count = 0
    # 初始化对象属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 对计数器进行累加
        Person.count += 1

p1 = Person('Tom', 23)
P2 = Person('Lily', 20)

print(f'一共创建了{Person.count}个对象')




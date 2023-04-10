# 案例2：lihua体重75.0公斤，lihua每次跑步会减掉0.10公斤，lihua每次吃东西体重增加0.20公斤。
# 输出lihua信息
class Person(object):
    # 属性
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    # 方法
    # 使用__str__输出信息
    def __str__(self):
        return f'姓名：{self.__name}，体重：{self.__weight:.2f}'

    # 跑步减重，限制体重的位数
    def run(self):
        self.__weight -= 0.10

    # 进食增重
    def eat(self):
        self.__weight += 0.20


# 实例化对象
Lihua = Person('Lihua', 75)
print(Lihua)

# 执行方法
Lihua.run()
print(Lihua)

Lihua.eat()
print(Lihua)

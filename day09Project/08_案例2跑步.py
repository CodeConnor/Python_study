# 案例2：lihua体重75.0公斤，lihua每次跑步会减掉0.10公斤，lihua每次吃东西体重增加0.20公斤。
# 输出lihua信息
class WeightChange(object):
    # 属性
    def __init__(self):
        self.__name = 'Lihua'
        self.__kg = 75

    # 方法
    # 跑步减重，限制体重的位数
    def run(self):
        self.__kg -= 0.10
        print(f'{self.__name}减重0.10kg，现体重{self.__kg:.2f}kg')

    # 进食增重
    def eat(self):
        self.__kg += 0.20
        print(f'{self.__name}增重0.20kg，现体重{self.__kg:.2f}kg')


# 实例化对象
Lihua = WeightChange()
Lihua.eat()
Lihua.run()






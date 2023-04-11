# 定义Car类，包含初始化属性和run方法
# 定义GasolineCar，重写run方法
# 定义ElectricCar，重写属性和方法
class Car(object):
    # 公共属性
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # 公共方法
    def run(self):
        print('Cars can run')


class GasolineCar(Car):
    # 自动继承父类的公共属性
    # 重写方法
    def run(self):
        # 强制继承父类的方法
        super().run()
        print('Cars run with gasoline')


class ElectricCar(Car):
    # 重写父类中的属性
    def __init__(self, brand, color, battery):
        # 强制继承父类中的brand、color属性，只重写battery属性
        super().__init__(brand, color)
        self.battery = battery

    # 重写方法
    def run(self):
        print('Cars run with electricity')


benz = GasolineCar('Benz', 'black')
benz.run()

tesla = ElectricCar('Tesla', 'green', 'Li-battery')
tesla.run()
print(tesla.brand)
print(tesla.color)
print(tesla.battery)

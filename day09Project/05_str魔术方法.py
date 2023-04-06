# 需求：定义一个汽车类，类实例化对象必须要拥有哪些属性？branc品牌、model型号、color颜色
# 当我们打印这个汽车类对象时，要求输出这辆车的相关信息
class Car(object):
    # 公共属性
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    # 公共方法__str__
    # 当对象被打印时,不会弹出对象所指向的内存地址,而是返回__str()__方法中的相关信息
    # 只能用return返回不能使用print，返回的数据必须是str类型
    def __str__(self):
        return f'brand:{self.brand}, model:{self.model}, color:{self.color}'


# 实例化
bmw = Car('BMW', '320', 'black')
print(bmw)

benz = Car('Benz', 'G', 'white')
print(benz)


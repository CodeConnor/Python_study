# 定义Fruit类
class Fruit(object):
    # 公共方法
    def juice(self):
        pass


# 定义子类，重写公共方法
class Apple(Fruit):
    def juice(self):
        print('i like apple juice')


class Orange(Fruit):
    def juice(self):
        print('i like orange juice')


class Watermelon(Fruit):
    def juice(self):
        print('i like watermelon juice')


# 定义一个公共接口service
def service(obj):
    # obj要求是一个实例化对象，可以传入苹果对象/橘子对象
    obj.juice()


# 实例化对象
apple = Apple()
orange = Orange()
# 传入对象
service(apple)
service(orange)
service(Watermelon())  # 或者不实例化对象，直接传入类

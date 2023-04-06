class Person(object):
    # 未来对象所拥有的公共属性，self不需要传参
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 公共方法
    def __del__(self):
        print('当del对象时，此魔术方法会自动触发')


# 函数执行结束自动触发__del__
p1 = Person('Tom', 23, 'male')
# 手工del对象触发
p2 = Person('Lily', 20, 'female')
del p2

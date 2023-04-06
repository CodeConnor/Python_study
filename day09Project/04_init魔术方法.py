# __init__ 初始化方法，在其他编程语言中也称为构造函数
class Person(object):
    # 未来对象所拥有的公共属性，self不需要传参
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 公共方法
    def speak(self):
        print(f'my name:{self.name}, age:{self.age}, gender:{self.gender}')

# 实例化+传参，self不需要传参
p1 = Person('Tom', 23, 'male')
print(p1.name)
print(p1.age)
print(p1.gender)
p1.speak()

p2 = Person('Lily', 20, 'female')
print(p2.name)
print(p2.age)
print(p2.gender)
p2.speak()

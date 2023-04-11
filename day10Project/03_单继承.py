# 定义Person类，具有公共方法：run
# 定义adult子类，继承Person
# 定义worker子类，继承adult
class Person(object):
    # 公共属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 公共方法
    def run(self):
        print('i can run！')


class Adult(Person):
    # 属性
    # 扩展方法
    def work(self):
        print('i can work!')


class Worker(Adult):
    # 扩展方法
    def relax(self):
        print('i want to relax!')


# 实例化，p1能使用Person和Adult的所有公共属性和方法
p1 = Adult('Tom', 19)
print(p1.name)
print(p1.age)
p1.run()
p1.work()

# 实例化，p2能使用所有父类和子类的方法
p2 = Worker('John', 22)
print(p2.name)
print(p2.age)
p2.run()
p2.work()
p2.relax()


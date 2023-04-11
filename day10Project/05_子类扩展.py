# 定义Animal类，eat、call方法
# 定义Cat、Dog类
class Animal(object):
    def eat(self):
        print('I can eat')

    def call(self):
        print('I can bark')


class Cat(Animal):
    # 重写父类方法
    def call(self):
        print('meow meow meow')


cat = Cat()
cat.eat()  # 没有重写方法，使用的是父类方法
cat.call()  # 调用父类方法时，使用的是重写后的方法


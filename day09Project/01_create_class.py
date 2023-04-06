# 案例：定义一个Person类，方法有eat和run
class Person(object):
    # 属性
    # 方法
    def eat(self):
        print('i can eat food')

    def run(self):
        print('i can run')

    def sleep(self):
        print('i can sleep all day')


# 实例化和调用
p1 = Person()
p1.eat()
p1.Sleep()
p1.run()

p2 = Person()
p2.eat()
p2.Sleep()
p2.run()

# 打印对象可查看内存地址
print(p1)
print(p2)
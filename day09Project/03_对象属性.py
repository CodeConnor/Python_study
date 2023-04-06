class Person(object):
    # 属性
    # 方法
    def eat(self):
        print('i can eat food')

    def run(self):
        print('i can run')

    def sleep(self):
        print('i can sleep all day')

    # 在类内部获取属性
    def print_info(self):
        print(f'姓名：{self.name}')
        print(f'年龄：{self.age}')


p1 = Person()
# 在类外部添加属性
p1.name = 'Tom'
p1.age = 20

# 在类外部获取属性
print(p1.name)
print(p1.age)

# 访问属性
p1.print_info()

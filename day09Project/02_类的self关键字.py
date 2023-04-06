# 1、定义一个类
class Person():
    # 定义一个方法
    def speak(self):
        print(self)


# 2、类的实例化（生成对象）
p1 = Person()

print(p1)
p1.speak()

p2 = Person()
print(p2)
p2.speak()
# print之后p1和self的结果相同，p2和self的结果相同，即证明self指向了实例对象本身

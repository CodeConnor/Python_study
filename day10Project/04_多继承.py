# 定义一个Laptop类
# 定义一个MobilePhone
# 定义一个Pad类，继承上两类的方法
class Laptop(object):
    def func1(self):
        print('I have strong performance!')


class MobilePhone(object):
    def func2(self):
        print('I have portability')


class Pad(Laptop, MobilePhone):
    pass


ipad = Pad()
ipad.func1()
ipad.func2()

# 查看Pad类的继承关系
# (<class '__main__.Pad'>, <class '__main__.Laptop'>, <class '__main__.MobilePhone'>, <class 'object'>)
print(Pad.__mro__)
# [<class '__main__.Pad'>, <class '__main__.Laptop'>, <class '__main__.MobilePhone'>, <class 'object'>]
print(Pad.mro())
# 从左到右依次继承

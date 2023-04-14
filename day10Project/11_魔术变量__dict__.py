# 使用__dict__将实例属性转换为字典
class A(object):
    # 类属性
    a = 10

    # 对象属性（实例属性）
    def __init__(self):
        self.b = 100


aa = A()
# 打印对象aa的转换结果
print(aa.__dict__)  # {'b': 100}

class Girl(object):
    # 定义私有属性
    def __init__(self, name):
        self.__name = name
        self.__age = 18

    # 在类的内部定义函数（接口）来访问私有属性
    # 接口
    def getName(self):
        return self.__name

    # 接口
    def getAge(self):
        return self.__age


# 实例化
p1 = Girl('Lily')
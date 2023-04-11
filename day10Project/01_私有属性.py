# 定义Staff类，定义私有属性salary
# 添加访问和设置接口
# 过滤salary异常数据
class Staff(object):
    # 属性
    def __init__(self, name):
        self.name = name
        self.__salary = 10000

    # 访问接口
    def get_salary(self):
        return self.__salary

    # 修改接口
    def set_salary(self, salary):
        # 判断输入数据是否合法，即过滤异常数据
        if not isinstance(salary, int):  # isinstance：判断salary是否是int类型
            print('数据类型不正确')
            return  # 不是int类型就结束接口的使用
        elif salary <= 0:  # 检查数据合理性
            print('数据范围不合理')
            return
        # 数据合理就能正常修改
        self.__salary = salary
        return self.__salary

p1 = Staff('Tom')
print(p1.get_salary())
p1.set_salary(0)
p1.set_salary('aa')
print(p1.set_salary(100000))


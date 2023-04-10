# 案例1：定义学生信息类，包含姓名、成绩属性，定义成绩打印方法
# 90分及以上显示优秀，80分及以上显示良好，70分及以上显示中等，60分及以上显示合格，60分以下显示不及格
class StuInfo(object):
    # 属性
    # 定义学生的私有属性
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    # 方法
    # 定义学生分数等级的划分方法
    def grade(self):
        if self.__score >= 90:
            print(f'姓名：{self.__name} 分数：{self.__score} 等级：优秀')
        elif self.__score >= 80:
            print(f'姓名：{self.__name} 分数：{self.__score} 等级：良好')
        elif self.__score >= 70:
            print(f'姓名：{self.__name} 分数：{self.__score} 等级：中等')
        elif self.__score >= 60:
            print(f'姓名：{self.__name} 分数：{self.__score} 等级：合格')
        else:
            print(f'姓名：{self.__name} 分数：{self.__score} 等级：不合格')


# 实例化对象
stu1 = StuInfo('Tom', 90)
stu1.grade()

stu2 = StuInfo('Lily', 80)
stu2.grade()

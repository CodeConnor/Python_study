# 案例：统计tool工具类生成的对象数量
class Tool(object):
    # 定义类属性
    count = 0

    # 定义对象属性
    def __init__(self, name):
        self.name = name
        # 计数器累加
        Tool.count += 1

    # 定义类方法（接口）
    @classmethod  # 装饰类方法
    def get_count(cls):
        return f'已实例化对象：{Tool.count}'


t1 = Tool('hammer')
t2 = Tool('axe')
t3 = Tool('nail')
# 调用类方法
print(Tool.get_count())

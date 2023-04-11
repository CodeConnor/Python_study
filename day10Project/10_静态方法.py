# 学生管理系统中的菜单功能
# 菜单功能是独立的
# 不需要调用其他方法或访问属性
class StudentsManager(object):
    # 定义菜单功能，静态方法
    @staticmethod
    def menu():
        print('-' * 40)
        print('            学生管理系统v1.1')
        print('【1】添加学生信息')
        print('【2】删除学生信息')
        print('【3】修改学生信息')
        print('【4】查询学生信息')
        print('【5】显示所有学生信息')
        print('【6】保存数据到文件')
        print('【7】加载数据到系统')
        print('【8】退出系统')
        print('-' * 40)


# 直接调用
StudentsManager.menu()
# 实例化后再调用
p1 = StudentsManager()
p1.menu()

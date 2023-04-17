# 使用类装饰器装饰comment函数
class Check():
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        # 添加额外功能
        input('请先登录：')
        # 调用comment函数本身
        self.__fn()


# 源函数
@Check
def comment():
    print('发表评论')


comment()

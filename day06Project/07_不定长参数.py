# 不定长位置参数
def func1(*args):
    print(args)


# 多种方式调用函数
func1()
func1(1)
func1(1, 3, 5)  # 返回元组


# 不定长关键词参数
def func2(**kwargs):
    print(kwargs)


func2()
func2(a=1)
func2(a=1, b=3, c=5)


# 两个一起用
def func3(*args, **kwargs):  # *args必须放在左边，**kwargs必须放在右边
    print(args)
    print(kwargs)


func3(1, 2, 3, a=4, b=5, c=6)  # *args接收位置参数，**kwargs接收关键词参数

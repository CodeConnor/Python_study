# 需求：给comment发表评论函数增加一个额外的功能（要求先登录，有了账号以后才能发表评论）
# 要求：不能改变现有comment函数，不能改变comment函数调用方式，还要增加一个登录功能
# 装饰器函数：
def login(fn):
    def inner():
        input('请先登录：')
        fn()
    return inner

# comment函数
@login
def comment():
    print('发表评论')

comment()

# ------------------------案例：求程序的执行时间--------------------------------
# 在不改变原有函数源代码以及调用方式的前提下，为其增加一个统计执行时间功能
# 装饰器函数：
import time
def timer(fn):
    def inner():
        start = time.time()  # 获取开始时间
        fn()  # 需要计算执行时间的程序
        end = time.time()
        print(f'该函数执行一共花费了{end - start:.3f}s')
    return inner
# 需要统计时间的函数
@timer
def demo():
    list1 = []
    for i in range(10000000):
        list1.append(i)

demo()




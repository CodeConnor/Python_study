# 导入多进程包
import multiprocessing
import time
# 任务a
def func_a(n):
    for i in range(n):
        print('正在执行任务a。。。')
        time.sleep(1)  # 休眠1秒，方便观察任务执行流程

# 任务b
def func_b(t):
    for i in range(3):
        print('正在执行任务b。。。')
        time.sleep(t)

# 程序执行入口
if __name__ == '__main__':
    # 创建子进程
    a_process = multiprocessing.Process(target=func_a, args=(3,))
    b_process = multiprocessing.Process(target=func_b, kwargs={'t': 1})  # 两种传参方式都可以使用
    # 启动子进程
    a_process.start()
    b_process.start()

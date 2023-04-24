# 导入多进程包
import multiprocessing
import time
# 任务a
def func_a():
    for i in range(3):
        print('正在执行任务a。。。')
        time.sleep(1)  # 休眠1秒，方便观察任务执行流程

# 任务b
def func_b():
    for i in range(3):
        print('正在执行任务b。。。')
        time.sleep(1)

# 程序执行入口
if __name__ == '__main__':
    # 创建子进程
    a_process = multiprocessing.Process(target=func_a)
    b_process = multiprocessing.Process(target=func_b)
    # 启动子进程
    a_process.start()
    b_process.start()
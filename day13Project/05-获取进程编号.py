# 导入模块
import os
import multiprocessing
import time


# 定义函数
def working():
    print(f'当前子进程编号:{os.getpid()}')
    print(f'当前子进程的父进程编号{os.getppid()}')

    for i in range(3):
        print('working...')
        time.sleep(1)


# 程序入口，主程序
if __name__ == '__main__':
    print(f'主进程编号：{os.getpid()}')
    # 创建子进程
    working_process = multiprocessing.Process(target=working)
    working_process.start()

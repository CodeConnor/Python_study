# 导入线程模块
import threading
import time


def func_a(n):
    for i in range(n):
        print('正在执行a...')
        time.sleep(0.5)


def func_b(t):
    for i in range(3):
        print('正在执行b...')
        time.sleep(t)


# 程序入口
if __name__ == '__main__':
    # 创建子线程
    a_thread = threading.Thread(target=func_a, args=(3,))
    b_thread = threading.Thread(target=func_b, kwargs={'t': 0.5})

    # 启动线程
    a_thread.start()
    b_thread.start()

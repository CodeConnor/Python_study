import time
import multiprocessing

def work():
    for i in range(10):
        print('working...')
        time.sleep(0.2)


# 程序入口
if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    # 设置守护进程
    work_process.daemon = True
    work_process.start()

    time.sleep(1)
    # 守护进程与强制销毁二选一
    # 主进程结束之前强制销毁子进程
    # work_process.terminate()
    print('主进程已结束！')

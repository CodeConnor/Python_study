import time
import threading

def work():
    for i in range(10):
        print('working...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建线程对象并设置守护线程, 方式一
    work_thread = threading.Thread(target=work, daemon=True)
    # 设置守护线程，方式二
    work_thread.setDaemon(True)  # work_thread.daemon = True

    time.sleep(1)

    print('主线程结束！')
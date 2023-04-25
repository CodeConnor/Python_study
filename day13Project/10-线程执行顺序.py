# 使用threading.current_thread()获取线程信息方法来判断线程执行顺序
import time
import threading

def getInfo():
    time.sleep(0.2)  # 时延，保证在主线程创建10个子进程后，子进程还未执行结束
    current_thread = threading.current_thread()
    print(current_thread)


if __name__ == '__main__':
    for i in range(10):
        # 创建子线程
        getInfo_thread = threading.Thread(target=getInfo)
        getInfo_thread.start()

import time
import threading

# 定义全局变量
my_list = []

def write():
    for i in range(3):
        my_list.append(i)
        print(f'add:{i}')
    print(f'write:{my_list}')

def read():
    print(f'read:{my_list}')

# 程序入口
if __name__ == '__main__':
    write_thread = threading.Thread(target=write)
    read_thread = threading.Thread(target=read)

    write_thread.start()
    read_thread.start()

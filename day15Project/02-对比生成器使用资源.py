import time  # 使用该模块计算程序执行时间
import memory_profiler as mem  # 使用该模块计算程序占用的内存


# 计算时间
def timer(fn):
    start = time.time()
    fn()
    end = time.time()
    return f'程序执行时间：{end - start}s\n'


# 计算内存
def memory_usage(fn):
    start = mem.memory_usage()
    fn()
    end = mem.memory_usage()
    return f'内存使用了：{end[0] - start[0]}MB\n'


# 使用生成器推导式
def generator1():
    square = (i ** 2 for i in range(10000000))


# 不使用生成器
def func1():
    square = [i ** 2 for i in range(10000000)]


if __name__ == '__main__':
    print(timer(func1))
    print(timer(generator1))
    print(memory_usage(func1))
    print(memory_usage(generator1))

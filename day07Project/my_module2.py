def func1():
    return 1


def func2():
    return 2


def func3():
    return 3


if __name__ == '__main__':  # 只有在当前页面运行__name__才会等于__main__
    print(__name__)
    print(func1())
    print(func2())
    print(func3())

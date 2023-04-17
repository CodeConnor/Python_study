# 声明局部变量
def outer():
    # 局部变量
    num = 10

    def inner():
        # 声明离inner最近的局部变量
        nonlocal num
        num = 100

    inner()
    print(num)


outer()


# 闭包与nonlocal的应用
def func():
    result = 0

    def inner(num):
        nonlocal result
        result += num
        print(result)

    return inner


fn = func()
fn(1)  # 1
fn(2)  # 3
fn(3)  # 6

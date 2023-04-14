# 使用闭包
def outer():
    # outer函数中的局部变量
    num1 = 100

    # 嵌套函数
    def inner():
        print(num1)

    # 返回内层函数
    return inner


fn = outer()  # 找到outer函数所在内存地址并立即执行其内部的代码，返回结果为inner函数，并赋值给fn
fn()  # 相当于inner()，即执行inner函数
print(outer)  # 打印outer函数所指向的内存地址
print(outer())  # 执行outer函数，然后打印执行结果，即打印inner函数所执向的内存地址
print(fn)  # 与上句相同
print(fn())  # 先执行fn()即执行inner函数，结果是100(print)，然后打印inner函数的返回结果，inner返回为None

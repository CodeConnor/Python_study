def greet(name):  # name一个形参
    # name作用域只在此函数内部有效,因为其是一个局部变量
    return 'hello,' + name


# 定义一个全局变量
name = '老王'
greet(name)  # 函调用时所指定的参数是一个实参,通常是一个全局变量

# 定义一个函数
def func(name, age, mobile):
    print(name)
    print(age)
    print(mobile)


# ①位置传参,根据函数定义时参数的位置传递参数的值(强调参数的位置,顺序不能颠倒)
func('Tom', 23, '10000')

# ②关键词传参,根据"参数=值方式来实现对参数的传递,优势:不需要考虑位置关系,只要参数名称没错,任何位置都可以
func(name='Jack', mobile='10010', age=19)

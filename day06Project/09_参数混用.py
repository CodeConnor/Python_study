# 四种参数混用
def func(a, b, *args, c=4, **kwargs):
    print(a, b)
    print(args)
    print(c)
    print(kwargs)


func(1, 2, 50, c=100, d=5, e=6)  # 此时传递默认值参数时需要写全


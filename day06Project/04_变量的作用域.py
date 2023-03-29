# 尝试修改全局变量
# num = 10
# def func():
#     num = 100
#
#
# func()
# print(num)  # 调用函数后发现无法修改

# 使用global修改全局变量
num = 10
def func():
    global num  # 从该行开始，以后使用的num都是全局变量
    num = 100


func()
print(num)  # 成功修改num

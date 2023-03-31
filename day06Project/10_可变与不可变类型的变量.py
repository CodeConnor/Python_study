# 定义函数
def func(num2, names2):
    num2 += 10  # 无法在局部作用域修改不可变类型的变量
    names2.append('Connor')  # 可以在局部作用域修改可变类型的变量


# 定义全局变量
num1 = 10
names1 = ['Herry', 'Jerry', 'Tom']
# 调用函数
func(num1, names1)

print(num1, names1)  # 10  ['Herry', 'Jerry', 'Tom', 'Connor']




# 导入自定义函数1
import my_module1
my_module1.sum_num(10, 20)

from my_module1 import sum_num
sum_num(10, 20)


# 导入自定义函数2
import my_module2  # 导入后直接运行不会出结果

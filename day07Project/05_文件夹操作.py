# 案例：准备一个static文件夹以及file1.txt、file2.txt、file3.txt三个文件
# ① 在程序中，将当前目录切换到static文件夹
# ② 创建一个新images文件夹以及test文件夹
# ③ 获取目录下的所有文件
# ④ 移除test文件夹
import os
os.chdir('static')  # 切换
print(os.getcwd())  # 查看当前目录
if not os.path.exists('images'):  # 判断是否存在
    os.mkdir('images')
if not os.path.exists('test'):
    os.mkdir('test')
print(os.listdir())  # 查看所有文件
os.rmdir('test')

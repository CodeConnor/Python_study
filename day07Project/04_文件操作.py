# 案例：把Python项目目录下的python.txt文件，更名为linux.txt，
# 查看效果，然后对这个文件进行删除操作。
import os
if os.path.exists('python.txt'):  # 判断文件是否存在，防止不存在时报错
    os.rename('python.txt', 'linux.txt')
os.remove('linux.txt')
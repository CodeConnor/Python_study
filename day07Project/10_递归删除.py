import shutil
import os
cwd = os.getcwd()
# 遍历当前工作目录中的所有文件和文件夹
for f in os.listdir():
    # 将路径和文件名组合
    filename = os.path.join(cwd, f)
    # 判断后缀是否是.txt
    if f.endswith('.txt'):
        # 删除文件
        os.remove(filename)

# 可简写为：
# # 获取当前目录中所有后缀为 '.txt' 的文件的完整路径
# txt_files = [os.path.join(cwd, f) for f in os.listdir(cwd) if f.endswith('.txt')]
#
# # 循环遍历所有后缀为 '.txt' 的文件，并使用 os.remove() 函数删除它们
# for txt_file in txt_files:
#     os.remove(txt_file)

# 指定要删除的文件夹
folders_del = ['py', 'static']
# 遍历文件夹
for folder in folders_del:
    # 加入删除提示
    try:
        # 递归删除
        shutil.rmtree(folder)
        print(f'文件夹{folder}删除成功')
    except Exception as e:
        print(f'文件夹{folder}删除失败，错误：{e}')


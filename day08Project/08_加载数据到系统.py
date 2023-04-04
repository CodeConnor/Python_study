import os

students = []
# global students
# 判断文件是否存在，防止打开文件报错
if not os.path.exists('students.txt'):
    print('【文件不存在，请先保存数据至文件！】')
else:
    f = open('students.txt', 'r', encoding='utf-8')
    content = f.read()
    # 判断文件是否为空
    if not content:
        print('【文件为空，请先保存数据至文件！】')
    else:
        # content为str，需要将其转换为list
        students = eval(content)
        print('【数据加载成功！】')


print(students)
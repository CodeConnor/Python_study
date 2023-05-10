# 实现一个可以递归删除指定目录下面的固定格式的文件的程序
# 示例： remove（myproject, 'pyc'） , 表示删除myproject目录中的所有以pyc文件结尾的文件
import os


def remove(path, postfix):
    # 判断路径是否正确
    if not os.path.isdir(path):
        print('目录路径不正确')
    else:
        # 遍历指定目录以及所有子目录
        for root, dirs, files in os.walk(path):
            # 遍历其中的所有文件
            for file in files:
                # 分开后缀与与文件名
                file_name, file_postfix = os.path.splitext(file)
                # 通过后缀名筛选需要删除的文件
                if file_postfix == '.' + postfix:
                    # 拼接文件路径
                    file_path = os.path.join(root, file)
                    # 删除文件
                    os.remove(file_path)
                    # 打印删除信息
                    print(f'{file_path}已删除！')


if __name__ == '__main__':
    remove('myproject', 'pyc')

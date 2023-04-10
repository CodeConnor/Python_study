# 案例：搬家具
# 1. 家具分不同的类型，并占用不同的面积
# 2. 输出家具信息时，显示家具的类型和家具占用的面积
# 3. 房子有存放物品列表和剩余的面积
# 4. 房子可以添加家具，如果房子的剩余面积可以容纳家具，则提示家具添加成功；否则提示添加失败
# 5. 输出房子信息时，可以显示房子的所存放家具、剩余面积
class Furniture(object):
    # 属性
    def __init__(self):
        name = input('Please enter the name of the furniture:')
        size = int(input('Please enter the area occupied by the furniture:'))
        self.__name = name
        self.__size = size
        # 定义房间的剩余面积，不用传参
        self.__area = 20  # 初始20

    # 方法
    # 输出房间信息
    def room(self):
        print(f'The available area of the current room is {self.__area}㎡')

    # 输出家具信息
    def __str__(self):
        return f'The {self.__name} takes up {self.__size}㎡'

    # 添加家具
    def add_furniture(self):
        if self.__area >= self.__size:
            self.__area -= self.__size
            print('Furniture added successfully')
        else:
            print('Insufficient remaining area, furniture addition failed')


i = ''
bed = Furniture()
while i != 'q':
    # 实例化对象
    print(bed)
    bed.add_furniture()
    bed.room()
    i = input("Enter 'q' to quit the program, or enter any other key to continue.\n:")

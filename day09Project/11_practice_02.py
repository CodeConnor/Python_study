# 案例：搬家具
# 1. 家具分不同的类型，并占用不同的面积
# 2. 输出家具信息时，显示家具的类型和家具占用的面积
# 3. 房子有存放物品列表和剩余的面积
# 4. 房子可以添加家具，如果房子的剩余面积可以容纳家具，则提示家具添加成功；否则提示添加失败
# 5. 输出房子信息时，可以显示房子的所存放家具、剩余面积

# 定义家具类
class Furniture(object):
    # 属性
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    # 方法
    # 输出家具信息
    def __str__(self):
        return f'The {self.__name} takes up {self.__size}㎡'

    # 定义公共接口，用于调用家具的信息
    def getUsedSize(self):
        return self.__size

    def getFurniture(self):
        return self.__name


# 定义房间类
class Home(object):
    # 属性
    def __init__(self, area):
        # 房间大小
        self.__area = area
        # 定义一个空列表用于存放家具的对象
        self.__items = []

    # 方法
    # 添加家具
    def addFurniture(self, item):  # item用于接收家具对象
        # 调用家具的接口
        used_size = item.getUsedSize()
        # 判断房屋空间是否足够
        if self.__area >= used_size:
            # 添加家具的对象进入房屋列表
            self.__area -= used_size
            self.__items.append(item)
            print('Furniture added successfully')
        else:
            print('Insufficient remaining area, furniture addition failed')

    # 输出房间信息
    def __str__(self):
        f_name = []
        for i in self.__items:
            f_name.append(i.getFurniture())
        home_info = f'Furniture placed in the house: {f_name}\nRemaining area: {self.__area}㎡'
        return home_info


# 添加循环条件和空列表
i = ''
list1 = []
while i != 'q':
    # 输入家具信息
    name = input('Please enter the name of the furniture:')
    size = int(input('Please enter the area occupied by the furniture:'))
    # 实例化
    f = Furniture(name, size)
    # 存储家具对象
    list1.append(f)
    i = input("Enter 'q' to quit the program, or enter any other key to continue.\n:")

# 实例化房屋对象
house1 = Home(20)
print(house1)
for i in list1:
    print(i)
    house1.addFurniture(i)
    print(house1)


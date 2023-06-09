# 定义一个star类(明星类)
# 使用init方法给对象添加属性
# 添加name = xxx，movie = yyy
# 定义方法playing()，打印“xxx 出演了 yyy”
# print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"
# 删除创建的对象，打印“期待xxx的新电影”
# 循环输入三个明星信息，之后再一起输出结果
class Star(object):
    # 属性
    def __init__(self, name, movie):
        self.__name = name
        self.__movie = movie
    # 方法
    def playing(self):
        print(f'{self.__name} starred in the movie {self.__movie}')

    def __str__(self):
        return f"{self.__name} is my idol, and I really enjoy his movie, '{self.__movie}'."

    def __del__(self):
        print(f"Looking forward to {self.__name}'s new movie.")


# jay = Star('Jay Chou', 'Initial D')
# print(jay.playing())
# print(jay)
#
# zrf = Star('Chow Yun Fat', 'God of Gamblers')
# zxc = Star('Stephen Chow', 'Kung Fu Hustle')

# 定义空列表用于存储对象
list1 = []
# 使用循环，输入信息
i = 1
while i <= 3:
    name = input('Please enter the name of the star:')
    movie = input('Please enter the movie in which the star appeared:')
    # 使用输入的信息实例化对象
    s = Star(name, movie)
    # 将对象存储进列表中
    list1.append(s)
    i += 1
# 循环使用方法
for s in list1:
    s.playing()
    print(s)

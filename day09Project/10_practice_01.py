# 定义一个star类(明星类)， 通过明星类创建一个zhou对象
# 使用init方法给对象添加属性
# 添加name = xxx，movie = yyy
# 定义方法playing()，打印“xxx 出演了 yyy”
# print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"
# 删除创建的对象，打印“期待xxx的新电影”
class Star(object):
    # 属性
    def __init__(self, name, movie):
        self.__name = name
        self.__movie = movie
    # 方法
    def playing(self):
        return f'{self.__name} starred in the movie {self.__movie}'

    def __str__(self):
        return f"{self.__name} is my idol, and I really enjoy his movie, '{self.__movie}'."

    def __del__(self):
        print(f"Looking forward to {self.__name}'s new movie.")

jay = Star('Jay Chou', 'Initial D')
print(jay.playing())
print(jay)

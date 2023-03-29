#  需求:请封装一个函数,用于接收list1与dict1的值,然后对其进行求和操作
list1 = [1, 2, 3]
dict1 = {'a': 4, 'b': 5}


def func(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    for value in kwargs.values():
        sum += value
    print(sum)


func(*list1, **dict1)

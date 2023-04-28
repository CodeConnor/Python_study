def generator(n):
    for i in range(n):
        print('开始生成数据...')
        yield i  # 每次执行到yield就会返回一个元素，并将程序暂停于此，下次执行从yield的下一句语句开始
        print('完成1次数据生成...')

g = generator(5)  # g是一个对象
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g1 = generator(6)
for i in g1:
    print(i)
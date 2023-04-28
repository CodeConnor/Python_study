# 推导式创建生成器
my_generator = (i * 2 for i in range(5))
print(my_generator)  # 生成器中保存的不是数据，而是对象，数据生成规则的对象

# 使用next()获取生成器中元素
value = next(my_generator)  # 调用1次next方法生成1个元素
print(value)

# 遍历生成器
for value in my_generator:
    print(value)
from pyecharts.faker import Faker

print(Faker.choose())  # ['草莓', '芒果', '葡萄', '雪梨', '西瓜', '柠檬', '车厘子']
print(Faker.values())  # [59, 135, 83, 61, 28, 143, 82]
# 选择特定的元素
print(Faker.cars)  # ['宝马', '法拉利', '奔驰', '奥迪', '大众', '丰田', '特斯拉']

# 参与游戏的角色有两个（玩家 与 电脑，人机对战），玩家手工出拳，电脑随机出拳，根据石头剪刀布判断输赢。
# 玩家：player（玩家手工输入石头0、剪刀1、布2）
# 电脑：computer（随机出拳）

# 随机模块的使用
# # 1. 导入模块
# import random
# # 2. 基于模块中的randint(start, stop)闭区间，规定随机数范围
# randnum = random.randint(0, 2)  # 0, 1, 2
# player = int(input('请出拳（玩家手工输入石头0、剪刀1、布2）：'))
# if (player == 0 and randnum == 1) or (player == 1 and randnum == 2) or (player == 2 and randnum == 0):
#     print('player win')
# elif player == randnum:
#     print('no winner')
# else:
#     print('player lose')
# print(f'computer：{randnum}')

# 改良：①不用数字表示出拳，用更直观的文字表示出拳；②引入循环，共计执行十次，记录玩家胜负的次数
import random  # 导入随机模块
# 定义胜负场数变量
win = 0
lose = 0
equal = 0
# 循环体，5次循环
i = 1
while i <= 5:
    # 展示玩家出拳
    player = int(input('请出拳（玩家手工输入石头0、剪刀1、布2）：'))
    if player == 0:
        print('player：石头')
    elif player == 1:
        print('player：剪刀')
    elif player == 2:
        print('player：布')
    else:
        print('出错拳！')
    # 显示电脑出拳
    randnum = random.randint(0, 2)  # 0, 1, 2
    if randnum == 0:
        print('computer：石头')
    elif randnum == 1:
        print('computer：剪刀')
    else:
        print('computer：布')
    # 输赢判断以及胜负场数记录
    if (player == 0 and randnum == 1) or (player == 1 and randnum == 2) or (player == 2 and randnum == 0):
        print('player win')
        win += 1
    elif player == randnum:
        print('no winner')
        equal += 1
    else:
        print('player lose')
        lose += 1
    i += 1  # 更新计数器
print(f'玩家胜{win} 平{equal} 负{lose}')


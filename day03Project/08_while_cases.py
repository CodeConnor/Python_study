# 需求：计算机从1 ~ 10之间随机生成一个数字，
# 然后提示输入数字，如果我们输入的数字与随机数相等，则提示恭喜你，答对了。
# 如果输入的数字比随机数大，则提示，猜大了。
# 反之，则提示猜小了，一共有3次机会。
import random
randnum = random.randint(1, 10)
i = 1
while i <= 3:
    usernum = int(input('请输入数字进行猜谜：'))
    if randnum == usernum:
        print('猜对了')
    elif randnum > usernum:
        print('猜小了')
    else:
        print('猜大了')
    i += 1


# 改良猜谜，不限制次数
import random
randnum = random.randint(1, 10)
while True:  # 无限次循环猜谜
    usernum = int(input('请输入数字进行猜谜：'))
    if randnum == usernum:
        print('猜对了')
        break  # 猜对后终止
    elif randnum > usernum:
        print('猜小了')
    else:
        print('猜大了')

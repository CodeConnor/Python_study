numstr = '0123456789'
# 截取234
print(numstr[2:5])
print(numstr[2:5:1])
print(numstr[-8:-5])
print(numstr[-8:-5:1])
# 0123
print(numstr[0:4])
print(numstr[:4])
print(numstr[-10:-6])
print(numstr[:-6])
# 123456789
print(numstr[1:])
print(numstr[-9:])
# 543210
print(numstr[5::-1])
# 截取整个字符串
print(numstr[:])
print(numstr[::])
# 字符串翻转
print(numstr[::-1])
# 截取所有偶数
print(numstr[0::2])
print(numstr[8::-2])
# 截取所有奇数
print(numstr[1::2])
print(numstr[:0:-2])
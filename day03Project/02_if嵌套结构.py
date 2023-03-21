# 案例：法律规定，车辆驾驶员的血液酒精含量小于 20mg/100ml 不构成酒驾；
# 酒精含量大于或等于 20mg/100ml 为酒驾；
# 酒精含量大于或等于 80mg/100ml 为醉驾。
# 编写 Python 程序判断是否为酒后驾车。

proof = int(input('车辆驾驶员的血液酒精含量为：'))
if proof >= 20:
    print('酒驾')
    if proof >= 80:
        print('醉驾')
else:
    print('不构成酒驾')
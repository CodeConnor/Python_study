# # 除数异常
# print(10 / 0)
#
# # 文件读取异常
# f = open('python.txt', 'r')
# content = f.readlines()
# print(content)

# 异常捕获案例，输入数字执行除法
num = int(input('请输入数字：'))
try:
    result = 100 / num
    print(result)
except:
    print('出现异常，执行B计划')

# 输出异常信息
try:
    result = 100 / num
    print(result)
except Exception as e:
    print(f'--日志：{e}--')  # 用print代替日志

# 加入else，finally
try:
    f = open('python[备份].txt', 'r', encoding='utf-8')
except:
    f = open('python[备份].txt', 'w', encoding='utf-8')
else:
    content = f.readlines()
    print(content)
finally:
    f.close()

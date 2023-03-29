# 定义一个testB函数
def testB():
    print('----- testB start -----')
    print('testB函数体代码...')
    print('----- testB end -----')


# 定义一个testA函数，在其中调用testB
def testA():
    print('----- testA start -----')
    testB()
    print('----- testA end -----')


# 调用testA函数
testA()

# 模拟使用ATM取款
# 银行 => ATM取款 => ①插卡②用户验证③输入取款金额④取款⑤打印账单

# 不使用私有方法时
class ATM1(object):
    def __card(self):
        print('插卡')

    def __id_verify(self):
        print('用户验证')

    def __input(self):
        print('输入取款金额')

    def __draw_money(self):
        print('取款')

    def __bill(self):
        print('打印账单')

    # 添加公共接口，实现取款操作
    def withdraw(self):
        self.__card()
        self.__id_verify()
        self.__input()
        self.__draw_money()
        self.__bill()


p1 = ATM1()
# 不使用私有方法时，完整取款流程需要调用5个方法
# p1.card()
# p1.id_verify()
# p1.input()
# p1.draw_money()
# p1.bill()
# ======================================================
# 使用私有方法简化程序
p1.withdraw()

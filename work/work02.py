# 定义一个程序员类 Coder ，
# 定义一个工作方法 work，一个睡觉方法 sleep, 一个幻想方法 imagine,
# 一个存款属性 money, 一个职位属性 title
# 要求:
# 1. 要求其中幻想方法与存款属性类型为私有方法和私有属性
# 2. 调用方法, 实现在类定义外部调用方法, 修改私有属性存款的值


class Coder(object):
    """程序员类"""
    def __init__(self, money, title):
        self.__money = money
        self.title = title

    def work(self):
        """工作方法"""
        print(f'{self.title}工作', end='')

    def sleep(self):
        """睡觉方法"""
        print(f'{self.title}睡觉')

    def __imagine(self):
        """幻想方法"""
        print(f'{self.title}幻想')

    def change_money(self, money):
        """修改存款方法"""
        self.__money = money
        print(f'修改后的存款为{self.__money}')

    def change_imagine(self):
        """在外部调用幻想方法"""
        self.__imagine()


# 实例化对象
zs = Coder(100000, '程序员')
# 调用方法
zs.work()
zs.sleep()
zs.change_imagine()
zs.change_money(200000)

print("*" * 30)
# 定义一个菜鸟类 Rookie 继承自程序员类 Coder, 覆盖重写程序员类中的 work 方法, 方法内容自定


class Rookie(Coder):
    """菜鸟类"""
    def work(self):
        print(f'{self.title}工作难')


# 实例化对象
ls = Rookie(10000, '实习程序员')
# 调用方法
ls.work()
ls.change_imagine()
ls.change_money(20000)
ls.sleep()

print("*" * 30)
# 定义一个大神类 God 继承自程序员类 Coder,
# 扩展重写程序员类中的 work 方法, 方法内容自定


class God(Coder):
    """大神类"""
    def work(self):
        super().work()
        print('so easy!')


# 实例化对象
ww = God(1000000, '高级程序员')
ww.work()
ww.sleep()
ww.change_money(2000000)
ww.change_imagine()
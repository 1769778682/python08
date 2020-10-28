class Father(object):
    """父类"""

    def __init__(self, name):
        self.__name = name

    def __driver(self):
        """驾驶方法"""
        print('开宝马')


class Son1(Father):

    def change_name(self, name):
        self.__name = name
        print(f'修改后的名字是{self.__name}')


# 需求1
xm = Son1('王')
# print(xm.__name)
# xm.__driver()
xm.change_name('李')

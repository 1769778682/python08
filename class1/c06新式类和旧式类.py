# 类的定义方式区分为：新式类和旧式类
# 新式类：定义类时，以 object 为基类：class 类名(object)
# 旧式类：定义类时，不以 object 为基类 class 类名：（）不推荐


class Demo1(object):  # Python3 的定义语法
    """新式类"""
    pass


class Demo2:  # Python2的定义语法，Python2在2020年1月已停止主动维护
    """旧式类"""
    pass



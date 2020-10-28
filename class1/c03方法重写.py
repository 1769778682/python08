# 现在两个类。父类和子类，
# 1.父类中拥有驾驶方法（开宝马），子类调用驾驶方法（骑自行车）
# 2.子类和女朋友一起开车


class Father(object):
    """父类"""

    def driver(self):
        """驾驶方法"""
        print('开宝马')


# 需求1
class Son1(Father):
    # 方法重写形式一：在子类中重新定义父类方法（方法名相同）即可
    def driver(self):
        """子类驾驶方法"""
        print('骑自行车')


# 需求2
class Son2(Father):
    # 方法重写形式一：在子类中重新定义父类方法（方法名相同）即可
    def driver(self):
        """子类驾驶方法"""
        # 通过 super 类，初始化超类对象并调用父类方法
        super().driver()  # 1.先获取父类方法实现
        print('和女朋友一起去兜风')  # 2.再实现自己的需求


# 需求1
xm = Son1()
xm.driver()  # 骑自行车（覆盖父类方法）
# 需求2
xm = Son2()
xm.driver()  # 开宝马和女朋友一起去兜风（扩展父类方法）
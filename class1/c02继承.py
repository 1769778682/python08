# 分别定义动物类/狗类/猫类/哮天犬类


class Animal(object):
    """动物类"""

    def eat(self):
        """吃方法"""
        print('动物类-吃')

    def drink(self):
        """喝方法"""
        print('动物类-喝')

    def run(self):
        """跑方法"""
        print('动物类-跑')

    def sleep(self):
        """睡觉方法"""
        print('动物类-睡')


class Dog(Animal):
    """狗类"""

    def shout(self):
        """叫方法"""
        print('狗-叫')


class Cat(Animal):
    """猫类"""

    def grab(self):
        """抓方法"""
        print('猫-抓')


class Xtq(Dog):
    """哮天犬类"""

    def fly(self):
        """飞天方法"""
        print('哮天犬-飞')


# 初始化狗对象
hsq = Dog()
hsq.eat()
hsq.drink()
hsq.run()
hsq.sleep()
hsq.shout()
# 初始化猫对象
tom = Cat()
tom.sleep()
tom.run()
tom.drink()
tom.eat()
tom.grab()
# 初始化哮天犬对象
xtq = Xtq()
xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()
xtq.fly()
xtq.shout()

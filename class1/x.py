class Test(object):

    def __init__(self, name, age):
        self.name = name
        self._age = age  # 单下划线开头的属性名：保护变量
        # 保护变量：是开发人员约定俗成的一种变量命名习惯，主要作用类似私有变量

    def eat(self):
        print(f'{self.name}吃东西')

    def __drink(self):  # 私有方法
        print('喝东西')


test1 = Test('xxx', 34)
test1.eat()
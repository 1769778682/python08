class Test(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def eat(self):
        print(f'{self.name}吃东西')

    def __drink(self):  # 私有方法
        print('喝东西')

    def chang_age(self, age):
        self.__age = age
        print(f'修改后的年龄为{self.__age}')


test1 = Test('xxx', 34)
test1.eat()
test1.chang_age(50)

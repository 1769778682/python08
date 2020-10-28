class Father1(object):
    @staticmethod
    def test1():
        print('父类1')

    @staticmethod
    def test():
        print('父类1test')


class Father2(object):
    @staticmethod
    def test2():
        print('父类2')

    def test(self):
        print('父类1')


class Son(Father2, Father1):
    pass


xm = Son()
xm.test1()
xm.test2()
xm.test()
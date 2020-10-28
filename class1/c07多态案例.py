class Dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def game(self):
        print(f'{self.name}快乐的玩耍')


class Xtq(Dog):

    def game(self):
        print(f'{self.name}飞到天上去玩耍')


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, x):
        print(f'{self.name}和{x.name}一起快乐玩耍')


dog = Dog('小七', 12)
xtq = Xtq('哮天犬', 13)
xm = Person('小明')
dog.game()
xtq.game()
xm.game_with_dog(dog)
xm.game_with_dog(xtq)

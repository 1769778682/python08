# 需求：
# 1. 士兵 许三多 有一把 AK47
# 2. 士兵 可以 开火
# 3. 枪 能够 发射 子弹
# 4. 枪 装填 装填子弹 —— 增加子弹数量
"""
1.先定义枪类
2.再定义士兵类
3.再将士兵跟枪联系
"""
"""
类名：枪（Gun）
属性：型号（model）
方法：发射子弹（launch） 装填子弹（）
"""


class Gun(object):
    """枪类"""

    def __init__(self, model):
        """型号属性"""
        self.model = model
        # 定义初始数量
        self.bullet_count = 0

    def add_bullet(self, count):
        """添加子弹方法"""
        self.bullet_count += count
        print(f'已添加{self.bullet_count}发子弹')

    def launch_bullet(self):
        if self.bullet_count <= 0:
            print('请装填子弹')
        else:
            self.bullet_count -= 1
            return f'{self.model}发射一发子弹,还剩{self.bullet_count}发子弹'


"""
士兵类名：士兵类（Soldier）
属性：名字（name） 枪（gun）
方法：开火（fire）
"""


class Soldier(object):
    """士兵类"""

    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self, count):
        if self.gun is None:
            print(f'{self.name}还没有枪哦！')
            return
        self.gun.add_bullet(count)
        ak = self.gun.launch_bullet()
        print(f'{self.name}使用{ak}')


# 实例化对象
# 调用方法
if __name__ == '__main__':
    AK47 = Gun("AK47")
    # AK47.launch_bullet()
    # AK47.add_bullet(30)
    xsd = Soldier('许三多')
    xsd.gun = AK47
    xsd.fire(30)
    # xsd.gun.add_bullet(0)

# 需求
# 1. 设计一个 Game 类
# 2. 属性：
# 定义一个 类属性 top_score 记录游戏的 历史最高分
# 定义一个 实例属性 player_name 记录 当前游戏的玩家姓名
# 3. 方法：
# 静态方法 show_help 显示游戏帮助信息
# 类方法 show_top_score 显示历史最高分
# 实例方法 start_game 开始当前玩家的游戏
# 4. 主程序步骤
# 1) 查看帮助信息
# 2) 查看历史最高分
# 3) 创建游戏对象，开始游戏


class Game(object):
    """游戏类"""
    top_score = 0

    def __init__(self, play_name):
        self.play_name = play_name

    # 静态方法
    @staticmethod
    def show_help():
        """游戏帮助信息"""
        print('帮助信息：请射击出现在屏幕内僵尸')

    # 类方法
    @classmethod
    def show_top_score(cls):
        """显示历史最高分"""
        print(f'游戏最高分是{cls.top_score}')

    # 实例方法
    def star_game(self):
        """开始游戏"""
        print(f'请{self.play_name}开始game')
        print('游戏分数统计中...')
        # 修改游戏分数，类名.属性名
        Game.top_score = 999


# 调用静态方法
Game.show_help()
# 调用类方法
Game.show_top_score()
# 实例化游戏对象
xm = Game('小明')
# 调用实例方法
xm.star_game()
# 调用类方法
Game.show_top_score()

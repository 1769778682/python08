# 示例需求
# 定义一个 工具类
# 每件工具都有自己的 name
# 需求 —— 知道使用这个类，创建了多少个工具对象？


class Tool(object):
    # 声明类属性，用来记录创建工具对象的次数
    count = 0

    @classmethod
    def tool_count(cls):
        print(f'创建了{cls.count}个工具')

    def __init__(self, name):
        self.name = name
        # 对类属性进行计数加一  类名.类属性
        Tool.count += 1


# 创建工具对象
tool2 = Tool('锤子')
tool1 = Tool('斧头')
tool3 = Tool('铁锹')
# 打印输出创建的工具对象个数
Tool.tool_count()
# 定义一个公司类 Company, 要求如下:
# 1. 定义类属性 company_name , 值为: 黑马程序员
# 2. 定义类方法 change_company_name , 实现可以修改类属性 company_name 的值为: 传智播客
# 3. 定义静态方法 show_company_info , 实现打印输出类属性 company_name 的值
# 4. 定义实例属性 name 和 age , 实例化操作时传入员工信息: 小明, 20
# 5. 定义实例方法 show_info , 实现打印输出: 员工姓名: 小明 年龄: 20岁 所属公司: 传智播客
# 6. 完成上述方法调用, 按照要求输出对应结果


class Company(object):
    """公司类"""
    company_name = '黑马程序员'

    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name

    @staticmethod
    def show_company_info():
        print(f'公司名称：{Company.company_name}')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'员工姓名:{self.name} '
              f'年龄:{self.age}岁 所属公司:{Company.company_name}')


if __name__ == '__main__':
    # 实例化对象
    xm = Company('小明', 20)
    Company.change_company_name('传智播客')
    Company.show_company_info()
    xm.show_info()

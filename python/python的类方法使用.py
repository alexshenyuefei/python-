# python的类充当js里对象,是基本的数据结构,可以存储属性.
class calculator(object):
    operand1 = 1
    operand2 = 2

    @classmethod
    def add(cls):
        # 全局变量在程序之中始终有定义的,局部变量在它的函数体内,以及嵌套的函数内始终有定义的.
        #  这里的变量operand1,opearand2在函数外,需要通过解释器传入的cls,指定外部对象(这里是calculator)访问
        cls.result = cls.operand1 + cls.operand2

calculator.add()
print(calculator.result)
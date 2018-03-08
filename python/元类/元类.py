class Myclass(object):
    pass

print(Myclass) # <class '__main__.Myclass'>,可以被print，所以它的类也是对象！既然类是对象，你就能动态地创建类

"""
在日常工作里面就会有这种动态创建类的需求
"""


def func(instance):
    print(instance.a, instance.b)
    print(instance.method_a(10))
"""
正常使用起来传入的instance是符合需求的（instance有a、b属性和method_a方法）
"""

"""
想单独调试func的时候，需要「造」一个例子，假如不用元类，应该是这样写
"""

def generate_cls(a, b):
    class Fake(object):
        def __init__(self):
            self.a = a
            self.b = b
        def method_a(self, n):
            return n
    return Fake
    # Fake.a = a
    # Fake.b = b
    # return Fake

ins = generate_cls(1, 2)()
print(ins.a, ins.b, ins.method_a(10))
func(ins)
"""
正常是这样调试Ins的

这不算是「动态创建」的：

1. 类名（Fake）不方便改变

2. 要创建的类需要的属性和方法越多，就要对应的加码，不灵活。
"""


"""
可以这样做
"""
def method_a(self, n):
    return n

ins = type('Fake', (), {'a': 1, 'b': 2, 'method_a': method_a})()
func(ins)

"""
创建自己的元类
Python3中
class Foo(object, metaclass=something...):
Python会使用你写的元类来创建Foo这个类
"""

"""
type还有一种完全不同的功能，动态的创建类。
type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
用来创建类的东东就是「元类」
如果你愿意，你可以把type称为「类工厂」。type是Python中内建元类，当然，你也可以创建你自己的元类。
"""

class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        #遍历属性字典，把不是__开头的属性名字变为大写
        newAttr = {}
        for name,value in future_class_attr.items():
            if not name.startswith("__"):
                newAttr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        # return type(future_class_name, future_class_parents, newAttr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, future_class_name, future_class_parents, newAttr)

        # 方法3：使用super方法
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, newAttr)


class Foo(object, metaclass = UpperAttrMetaClass):
    bar = 'bip'
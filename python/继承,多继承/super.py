"""
super().方法和父类没有实质性的关联
super()按照当前对象的MRO 列表顺序,遍历查找要调用的方法.
"""
"""
super原理
def super(类名, self或者cls):
    mro = self或者cls.__class__.mro() 查找cls或者self的mro列表
    return mro[mro.index(类名) + 1],返回下一个mro列表中的要调用对象
"""
# 案例
"""
继承关系
      Base
      /  \
     /    \
    A      B
     \    /
      \  /
       C
"""
class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")


class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__() # 不要一说到 super 就想到父类！super 指的是 MRO 中的下一个类！ ,这里会调用B的__init__
        print("leave A")


class B(Base):
    def __init__(self):
        print("enter B")
        super(B,self).__init__()
        print("leave B")

class C(A,B):
    def __init__(self):
        print("enter C")
        super(C,self).__init__()
        print("leave C")
        print(C.__mro__)
c = C()

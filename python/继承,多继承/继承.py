"""
调用的方法如果自己没写过,只能调用继承得来的方法.
效果相当于在子类的上下文环境中再执行一遍父类方法的代码
或者说效果是把这部分代码复制到子类中再执行一遍
"""

class P(object): # parent class 父类
    f = "P"
    @classmethod
    def foo(cls):
        print(cls.f)


class C(P): # child class 子类
    f = "C"

C.foo() # 打印结果是C,说明执行继承得来的方法的上下文环境是子类的环境



b = P()
c = C() # 实例化子类
print(c.__class__) # <class '__main__.C'> 实例化对象是由C类创建的,显示所属的类名
print(C.__bases__) # (<class '__main__.P'>,) 类C的父类是P

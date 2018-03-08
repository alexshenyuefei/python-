class MyClass(object):
    def __new__(cls, *args, **kwargs):  # 类的方法,作用是新建一个对象,并将对象赋值给self变量
        print(locals())  # {'kwargs': {}, 'args': (), 'cls': <class '__main__.MyClass'>}局部变量是这些
        return object.__new__(cls)

    def __init__(self):
        print(locals())  # {'self': <__main__.MyClass object at 0x0000019BB466C710>}

a = MyClass()
print(a)  # <__main__.MyClass object at 0x0000019BB466C710> 将本次新建的对象(类中的self)传递给a


# 调用类创建(新建)实例对象,类内部是先执行__new__(cls)类方法,新建一个对象,将新建对象引用赋值给self变量
# 再执行实例方法__init__(self)(构造器)
# 实例方法的的参数都要显式传入(self)-新建对象,self.变量名=值,实际上是将值保存在self的属性中
# a和类Myclass中局部变量self指向相同的对象(内存地址相同)，说明a = MyClass(),实现了将新建对象(类中叫self)引用传递给a变量.
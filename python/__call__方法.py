# 类创建后的对象正常是不能调用的,自己定义了__call__方法后,对象被调用,会使用__call__方法

class MyClass(object):

    def __call__(self, *args, **kwargs):
        print('hello world')


a = MyClass()
a()
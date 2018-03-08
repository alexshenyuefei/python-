class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance # 这个就是每个对象的self,现在每次都返回同一个cls._instance,即同一个self,同一片存储空间.


a = Singleton()
b = Singleton()
print(a is b)

# 元类创建单例
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass2(object):
    __metaclass__ = Singleton2
    """
    设置有__metaclass__这个属性
    """
    a = 1


one = MyClass2()
two = MyClass2()

print(id(one))  # 31495472
print(id(two)) # 31495472
print(one == two)  # True
print(one is two)  # True


# 装饰器类实现单例
def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class MyClass3(object):
    a = 1


one = MyClass3()
two = MyClass3()

print(id(one))  # 29660784
print(id(two)) # 29660784
print(one == two)  # True
print(one is two) # True
class Myclass(object):
    pass

a = Myclass()
a.x = "123"
print(hasattr(a, "x"))  #hasattr(object,name)判断对象是否有name特性
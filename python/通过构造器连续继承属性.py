# 继承就是子对象找不到的属性,方法去父对象找,父对象找不到去父对象的父对象找.直到父对象的父对象是object.
# 但是子对象重写属性、方法时,父对象的属性和方法不起作用(被重写覆盖了),这时候要重新调用父对象的方法.(super)
class MyClass(object):
    def __init__(self):
        self.x = "x"
        self.y = "y"
        self.__f = "y"

    def g(self):
        self.g = "g函数"

class MyClassTwo(MyClass):
    def __init__(self):
        super(MyClassTwo, self).__init__()  # super要放在最前面,防止继承的属性覆盖现有属性
        super(MyClassTwo, self).g()     # superhan函数实际是将MyclassTwo和self绑定,调用父类的g函数
        self.x = "class2的x"

a = MyClassTwo()
print(a.x)
print(a.g)
b = MyClass()
print(b._MyClass__f)  #__设置为私有属性,无法在外部访问,也就无法重写,硬要访问,通过名字重整后访问.
print(a.__class__())
print(type(a))
print(type("233"))


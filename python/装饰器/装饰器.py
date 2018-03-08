"""
使用装饰器时，有一些细节需要被注意。
例如，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）。
functools.wraps把原函数的元信息拷贝到装饰器函数中，这使得装饰器函数也有和原函数一样的元信息
"""
import functools
def makeBold(fn):
    @functools.wraps(fn)
    def wrapped(arc):
        return "<i>" + fn(arc) + "</i>"
    return wrapped



@makeBold
def test1(arc):
    print(arc)
    return "hello world-1"

"""
本质是执行装饰器函数,再由装饰器调用执行本函数
"""
print(makeBold(test1)('arc'))
print(test1('arc'))

print(test1.__name__) # @functools.wraps(fn)没有这个的话,函数的名字会变成wrapped

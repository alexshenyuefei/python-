def makeBold(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped



@makeBold
def test1():
    return "hello world-1"

"""下面两行代码从执行效果上是等价的,是在test1()的上下文环境执行装饰器函数"""
print(makeBold(test1)())
print(test1())
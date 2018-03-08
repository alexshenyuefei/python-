def counter(start_at=0):
    count = start_at

    def incr():
        nonlocal count
        count +=1
        return count
    return incr

a = counter(10)  #定义一个计数器从10开始计数,这个闭包函数返回一个闭包函数的内嵌函数对象incr
print(a())   #内嵌函数对象再次调用

"""
为什么a = counter(10)调用不会释放内存呢?详见js作用域链笔记那一块
简单来说返回的incr对象,是counter函数局部变量对象的一个值.
counter函数局部变量对象有incr这一个引用,所以不会被释放.
每个函数执行时,会新建一个对象来储存函数的局部变量.正常调用结束后会释放.
但是如果局部变量被储存在函数的属性,或者返回一个内嵌函数对象时,这个储存函数局部变量的对象不会被释放.
"""
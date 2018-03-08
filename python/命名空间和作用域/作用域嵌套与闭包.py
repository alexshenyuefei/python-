"""
定义函数是单纯的名称绑定(将函数绑定到名称)，因此在函数内部也可以定义新的函数
作用域嵌套只与定义时的嵌套关系有关，与调用无关；名称不会解析到调用时的作用域中
"""
def add_func(a):
    def _add(b):
        print("b",b)
        return a + b
    return _add

a = add_func(1)
print(a(1))    # 2
print(a(2))    # 3


"""
名称解析到具体的值是在运行时进行的
闭包中包含的外部函数作用域中的名称，对应的值随外部函数作用域中该名称绑定的值而变化
"""

def func():
    a = 1
    print(a)
    def func2():
        return a
    a = 2
    print(a)
    return func2

func()()   # 2

"""
可以利用默认参数绑定的规则（在定义时进行绑定）来改变作用域，从而保存当前的值：
"""
def multipliers(n):
    funcs = []
    for i in range(0,n):
        def _func(b, i = i):   # 默认参数保存了当前的i的值，
                               # 同时改变i的作用域
            return i * b
        funcs.append(_func)
    return funcs

ms = multipliers(10)
ms[2](3)   # 6, 2 * 3

"""
函数内调用其他函数的过程，是首先将要调用的函数名称解析到对应的函数对象，
然后执行函数对象，
解析函数名称这一步也是在运行时进行的
因此，函数内部可以调用尚未定义的函数，包括自己
"""

def a(n):
    return b(n-1) if n else 0
def b(n):
    return a(n-1) if n else 1
def c(n):
    return c(n-1) + c(n-2) if n > 2 else 1

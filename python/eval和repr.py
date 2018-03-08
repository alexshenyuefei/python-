# eval函数将字符串当成有效Python表达式来求值，并返回计算结果
x = 1
print(eval('x+1'))
print(help(eval))

# repr函数,将Python的变量和表达式转换为字符串表示
"""
repr(obj, /)
    Return the canonical string representation of the object.
    返回字符串对象的规范表示
    For many object types, including most builtins, eval(repr(obj)) == obj.
"""
# print(help(repr))
print(eval(repr(x)))
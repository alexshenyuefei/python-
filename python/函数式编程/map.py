# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到可迭代对象的每个元素，并把结果作为新的Iterator返回。

"""
可迭代对象的本质
可迭代对象通过__iter__方法向我们提供一个迭代器，我们在迭代一个可迭代对象的时候，
实际上就是先获取该对象提供的一个迭代器，然后通过这个迭代器来依次获取对象中的每一个数据。
那么也就是说，一个具备了__iter__方法的对象，就是一个可迭代对象。

一个实现了__iter__方法和__next__方法的对象，就是迭代器。
"""

def f(x):
    return x*x


r = map(f,range(10))
print(list(r))

L = []
for n in range(10):
    L.append(f(n))
print(L)
"""
不需要map()函数，写一个循环，也可以计算出结果：
从上面的循环代码，不能明白“把f(x)作用在list的每一个元素并把结果生成一个新的list
"""

"""
map()作为高阶函数，事实上它把运算规则抽象了，
我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串
"""

a = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)
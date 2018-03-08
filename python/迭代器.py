"""
可迭代对象就是用于迭代操作（for 循环）的对象
它像列表一样可以迭代获取其中的每一个元素，任何实现了 __next__ 和__iter__方法 （python2 是 next）的对象都可以称为可迭代对象。
它与列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算（lazy evaluation）方式返回元素
因为它并没有把所有元素装载到内存中，而是等到调用 next 方法时候才返回该元素
按需调用 call by need 的方式，本质上 for 循环就是不断地调用迭代器的next方法
"""

print('hello world')
print('hello world')
class Fib:
    def __init__(self, n):
        self.prev = 0
        self.cur = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            value = self.cur
            self.cur = self.cur + self.prev
            self.prev = value
            self.n -= 1
            return value
        else:
            raise StopIteration()

f = Fib(10)
print([i for i in f])
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""
可迭代对象就是用于迭代操作（for 循环）的对象
它像列表一样可以迭代获取其中的每一个元素，任何实现了 __next__ 和__iter__方法 （python2 是 next）的对象都可以称为可迭代对象。
它与列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算（lazy evaluation）方式返回元素
因为它并没有把所有元素装载到内存中，而是等到调用 next 方法时候才返回该元素
按需调用 call by need 的方式，本质上 for 循环就是不断地调用迭代器的next方法
"""
"""
实现了__iter__和__next__方法的类就是迭代器
对于for循环同一个生成器只能来一次
而迭代器可以来n次循环,本质是调用__iter__方法,
迭代器都会重新执行__iter__一次

生成器是更容易写的迭代器
"""
# 这样的Fib只能来一次for循环因为,第二次时候self.n已经不满足条件了
class Fib:
    def __init__(self, n):
        self.prev = 0
        self.cur = 1
        self.n = n
        super().__init__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            self.prev,self.cur = self.cur,self.prev+self.cur
            self.n -= 1
            return self.prev
        else:
            raise StopIteration()


# 这样的fib可以来两次for循环,因为每次执行for都会执行__iter__一次,再次指定self的值
class Fib(object):
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

f = Fib(10)
for i in f:
    print(i)

for i in f:
    print(i)
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
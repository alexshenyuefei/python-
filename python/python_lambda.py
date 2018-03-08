# python的lambda是在执行时候绑定的
def MyFunc():
    a = 15
    b = lambda: a + 1
    print(b())
    a = 16
    print(b())
"""
lambda表达式在Python当中和定义函数是完全等效的，
A = lambda a: a
def A(a):
    return a
这两者等价.

类似js中A =function(a){
    return a;
} 
所以lambda表达式当中引用外部变量的时候，规则与函数中引用外部变量完全相同
当函数嵌套定义时，外层函数中变量的作用域会延伸到内部函数中，除非内部函数重新对这个变量进行了赋值。
上面的例子中，b这个lambda表达式当中的a变量，是绑定到MyFunc中的a变量的，所以在外面修改了a的值之后，b的运行结果会随之改变。这在很多时候是很方便的。
"""


my_funcs = []
"""
给my_funcs里面加入了10个lambda函数
每个lambda表达式分别代表与一个特定数相乘
然而最后我们发现我们所有创建的lambda表达式，都是跟9相乘。
lambda表达式当中绑定的i变量是外层的i变量，循环结束之后，这个变量变成了9，
所以所有的lambda表达式当中都引用的是这个9，而不是创建lambda表达式时当时的值。
因为python中for循环并没有单独作用域.i一直就是那一个i.0-9都是那一个内存地址的i
名称解析到具体的值是在运行时进行的
解决这个问题，我们需要把lambda表达式里面的变量绑定到一个独立的作用域。以前我常用的一种方法是这样的：
"""
for i in range(0, 10):
    my_funcs.append(lambda x: i * x)
print("*"*10)
# print(my_funcs[7])
print(my_funcs[7](3))

my_funcs = []
def _create_func(i):
    # lambda表达式中的i的绑定，从外层的i，变成了_create_func中的i，它的作用域在_create_func中,每次调用i的内存地址都不一样.
    return lambda x: i * x
for i in range(0, 10):
    my_funcs.append(_create_func(i))

print(my_funcs[7](3)) # 21

my_funcs = []
for i in range(0, 10):
    # lambda实际就是一个函数,等价于def 匿名函数,这里的i是匿名函数的参数i了
    # 名称解析到具体的值是在运行时进行的
    my_funcs.append(lambda x, i = i: i * x)

print(my_funcs[7](3)) # 21

if __name__ == '__main__':
    MyFunc()
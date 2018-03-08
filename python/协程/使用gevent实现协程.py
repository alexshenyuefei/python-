import gevent
import time
"""
gevent实现了第一个函数等待响应阻塞时,将这个函数自动注册回调函数,
切换到下一个函数执行,等到系统收到第一个函数的响应时,暂停此时执行的函数,
重新执行第一个函数.
yield语句在python中可以保存执行状态,并且存贮中间值.
"""


def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        # time.sleep(1)
        gevent.sleep(1)


g1 = gevent.spawn(f, 10)
g2 = gevent.spawn(f, 10)
g3 = gevent.spawn(f, 10)

g1.join()
g2.join()
g3.join()
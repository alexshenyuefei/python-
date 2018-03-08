# 生产一个消费者消费一个
# generator可以在执行过程中多次返回，所以它看上去就像一个可以记住执行状态的函数
# “子程序就是协程的一种特例。”


def producer(c):
    n = 0
    while n < 5:
        n += 1
        print('生产第%d个' % (n,))
        # 此处调用消费者
        if n == 1:
            c.__next__() #生成器第一次调用要send(None)或者c.__next__()
            a = c.send(n)
        else:
            a = c.send(n)
        print('消费者说%s' %a)
    c.close()


def customer():
    r = ''
    while True:
        a = yield r
        print('消费者消费了第%d个' % a)
        r = 'OK'

c = customer()
producer(c)
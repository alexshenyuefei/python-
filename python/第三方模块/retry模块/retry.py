# retrying模块需要安装
"""
retrying是一个 Python的重试包，
可以用来自动重试一些可能运行失败的程序段。
retrying提供一个装饰器函数retry，被装饰的函数就会在运行失败的条件下重新执行
"""
from retrying import retry

@retry(stop_max_attempt_number=3) #被装饰的函数如果执行，如果触发异常,会重新执行2次.
def print_hello_world():
    print('hello world')
    assert 1 == 0

print_hello_world()
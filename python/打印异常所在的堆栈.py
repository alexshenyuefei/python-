"""
python的异常类中是没有堆栈信息的，要记录堆栈最简单的办法是使用logging包，这包就是用来程序运行日志的。
"""
import logging
LOG_FILENAME = './log.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,)
logging.debug('This message should go to the log file')
import traceback

def fun(a,b):
    return a/b
try:
    fun(1,0)
except Exception:
    logging.warning('something ', exc_info = True)
    # logging.exception('出现异常拉',)
    # traceback.print_exc() #单纯只是打印,不会影响程序继续执行


import time
time.sleep(1)
print('hello')
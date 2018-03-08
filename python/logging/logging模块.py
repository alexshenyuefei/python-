# import logging
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warn message')
# logging.error('error message')
# logging.critical('critical message')

"""
默认情况下，logging模块将日志打印到屏幕上(stdout)，日志级别为WARNING(即只有日志级别高于WARNING的日志信息才会输出)，
日志格式如下所示：
WARNING  :   root            :warn message
日志级别  :   Logger实例名字  :日志消息内容

"""

"""
简单配置
日志级别 从小到大

级别                      何时使用
DEBUG       详细信息，典型地调试问题时会感兴趣。
INFO        证明事情按预期工作。
WARNING     表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。
ERROR       由于更严重的问题，软件已不能执行一些功能了。
CRITICAL    严重错误，表明软件已不能继续运行了。
"""
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='./loggers.log',
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
               )

"""
可以通过logging.getLogger(name)获取logger对象，
如果不指定name则返回root对象，多次使用相同的name调用getLogger方法返回同一个logger对象。
"""
logger1 = logging.getLogger(__name__)#给这个logger1对象取名字
# logger1 = logging.getLogger('chat gui')#给这个logger1对象取名字,通常取名要有意义

if __name__ == '__main__':
    print(__name__)
    # Logger.setLevel(lel): 指定最低的日志级别，低于lel的级别将被忽略。
    logger1.setLevel(logging.WARNING)
    logger1.warning("这是个警告的日志")


    # logging.warning("这是个警告的日志")
    logger1.info("this is info")
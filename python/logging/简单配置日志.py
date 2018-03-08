import logging

logging.basicConfig(filename='log.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.INFO)
logger1 = logging.getLogger(__name__)
logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')

logging.critical('critical message')
logger1.error('logger1  logger1  logger1  logger1') # 2017-12-27 00:04:15 AM - __main__ - ERROR -简单配置日志:  logger1  logger1  logger1  logger1
logging.error('logging  logging   logging') # 2017-12-27 00:04:15 AM - root - ERROR -简单配置日志:  logging  logging   logging

"""
输出：
发现当前工作目录下生成了logger.log
通过level=logging.INFO设置日志级别为INFO,所以日志级别大于info的都写入了
"""
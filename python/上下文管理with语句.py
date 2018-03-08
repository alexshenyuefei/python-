#with用于 数据库连接,锁分配,信号量加减,状态管理,打开/关闭文件,异常处理,
"""
类似try-except-finally , with 语句也是用来简化代码的,这与用try-except 和try-finally
所想达到的目的前后呼应.try-except 和try-finally 的一种特定的配合用法是保证共享的资源的
唯一分配,并在任务结束的时候释放它.比如文件(数据,日志,数据库等等),线程资源,简单同步,数
据库连接,等等. with 语句的目标就是应用在这种场景.
with 语句的目的在于从流程图中把 try,except 和finally 关键字和资源分配释放相关
代码统统去掉, 而不是像 try-except-finally 那样仅仅简化代码使之易用. with 语法的基本用法
看上去如下:
with context_expr [as var]:
    with_suite
它仅能工作于支持上下文管理协议(context managementprotocol)的对象.
这显然意味着只有内建了"上下文管理"的对象可以和with 一起工作
Edit By Vheavens
 file
 decimal.Context
 thread.LockType
 threading.Lock
 threading.RLock
 threading.Condition
 threading.Semaphore
 threading.BoundedSemaphore
"""

with open('/etc/passwd', 'r') as f:
    """
    它会完成准备工作,
    比如试图打开一个文件,如果一切正常,把文件对象赋值给f.然后用迭代器遍历文件中的每一行,当
    完成时,关闭文件.无论的在这一段代码的开始,中间,还是结束时发生异常,会执行清理的代码,此
    外文件仍会被自动的关闭.
    Python对with的处理还很聪明。基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
举例说明
    """
    for eachLine in f:
        # ...do stuff with eachLine or f...
        """
        因为已经从你手边拿走了一堆细节,所以实际上只是进行了两层处理:
        第一,发生用户层 —— 和 in 类似,你所需要关心的只是被使用的对象
        第二,在对象层.既然这个对象支持上下文管理协议,它干的也就是"上下文管理".
        """
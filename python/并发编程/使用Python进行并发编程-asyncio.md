http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-asyncio%E7%AF%87/

### 前言

在Python 2的时代，高性能的网络编程主要是使用Twisted、Tornado和Gevent这三个库，但是它们的异步代码相互之间既不兼容也不能移植。如上一节说的，Gvanrossum希望在Python 3 实现一个原生的基于生成器的协程库，其中直接内置了对异步IO的支持，这就是asyncio，它在Python 3.4被引入到标准库。

Python 3.5添加了async和await这两个关键字，分别用来替换`asyncio.coroutine`和`yield from`。自此，协程成为新的语法，而不再是一种生成器类型了。事件循环与协程的引入，可以极大提高高负载下程序的I/O性能。除此之外还增加了`async with`(异步上下文管理)、`async for`(异步迭代器)语法。特别说的是，在新发布的Python 3.6里面终于可以用[异步生成器](https://www.python.org/dev/peps/pep-0525/)了！

顺便说一下Twisted。虽然在之前的公司Twisted使用的还挺广泛，它的Reactor、Factory、Deferred、Protocol等编程的思想很有启发性，在当时已经非常先进了，而asyncio也借鉴了一部分。但是它太重、大量的回调（Javascript工程师很容易接受，比如Deferred，小明我不喜欢）、没有及时更新的中文相关的技术文档和书籍所以学习曲线较高、没有更多的公司出来分享对应的实践，再加上协程的冲击，最近1-2年已经很少看到它的身影，不建议新人再去学习它了。


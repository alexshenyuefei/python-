https://www.cnblogs.com/yuanchenqi/articles/5755198.html

redis教程:http://www.runoob.com/redis/redis-lists.html

## 缓存之redis



redis是一个key-value[存储系统](http://baike.baidu.com/view/51839.htm)。和Memcached类似，它支持存储的value类型相对更多，包括string(字符串)、list(列表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）.

这些[数据类型](http://baike.baidu.com/view/675645.htm)都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。

> mysql中原子性:事务被视为一个不可分割最小工作单元,事务中所有操作要么全部成功,要么全部回滚,不可执行其中一部分操作.



在此基础上，redis支持各种不同方式的排序。与memcached一样，为了保证效率，数据都是缓存在内存中。区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。



一、Redis安装和基本使用

> ```
> wget http://download.redis.io/releases/redis-3.0.6.tar.gz
> tar xzf redis-3.0.6.tar.gz
> cd redis-3.0.6
> make
> ```

启动服务端

> ```
> src/redis-server
> ```

启动客户端

> ```
> src/redis-cli
> redis> set foo bar
> OK
> redis> get foo
> "bar"
> ```



二、Python操作Redis

> ```
> sudo pip install redis
> or
> sudo easy_install redis
> or
> 源码安装
>  
> 详见：https://github.com/WoLpH/redis-py
> ```

#### 发布订阅和简单的消息队列区别

发布订阅会将消息发送给所有的订阅者，而消息队列中的数据被消费一次便消失。所以，RabbitMQ实现发布和订阅时，会为每一个订阅者创建一个队列，而发布者发布消息时，会将消息放置在所有相关队列中。

API使用

redis-py 的API的使用可以分类为：

- 连接方式
- 连接池
- 操作
  - - String 操作
    - Hash 操作
    - List 操作
    - Set 操作
    - Sort Set 操作
- 管道
- 发布订阅

#### 1、操作模式

redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import redis
 
r = redis.Redis(host='10.211.55.4', port=6379)
r.set('foo', 'Bar')
print r.get('foo')
```



#### 2、连接池

redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import redis
 
pool = redis.ConnectionPool(host='10.211.55.4', port=6379)
 
r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print r.get('foo')
```



3.操作



String操作，redis中的String在在内存中按照一个name对应一个value来存储



set(name, value, ex=None, px=None, nx=False, xx=False)

> ```
> 在Redis中设置值，默认，不存在则创建，存在则修改
> 参数：
>      ex，过期时间（秒）
>      px，过期时间（毫秒）
>      nx，如果设置为True，则只有name不存在时，当前set操作才执行
>      xx，如果设置为True，则只有name存在时，当前set操作才执行
> ```



setnx(name, value)

```
设置值，只有name不存在时，执行设置操作（添加）
```



setex(name, value, time)

> ```
> # 设置值
> # 参数：
>     # time，过期时间（数字秒 或 timedelta对象）
> ```



psetex(name, time_ms, value)

```
# 设置值
# 参数：
    # time_ms，过期时间（数字毫秒 或 timedelta对象）
```



mset(*args, **kwargs)

```
批量设置值
如：
    mset(k1='v1', k2='v2')
    或
    mset({'k1': 'v1', 'k2': 'v2'})
```



get(name)

```
#获取值
```

mget(keys, *args)

```
#批量获取
#如：
    mget('ylr', 'wupeiqi')
   # 或
    r.mget(['ylr', 'wupeiqi'])
```

getset(name, value)

```
#设置新值并获取原来的值
```

getrange(key, start, end)

```
# 获取子序列（根据字节获取，非字符）
# 参数：
    # name，Redis 的 name
    # start，起始位置（字节）
    # end，结束位置（字节）
```

setrange(name, offset, value)

```
# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
# 参数：
    # offset，字符串的索引，字节（一个汉字三个字节）
    # value，要设置的值
```





setbit(name, offset, value)

```python
# 对name对应值的二进制表示的位进行操作
 
# 参数：
    # name，redis的name
    # offset，位的索引（将值变换成二进制后再进行索引）
    # value，值只能是 1 或 0
 
# 注：如果在Redis中有一个对应： n1 = "foo"，
        那么字符串foo的二进制表示为：01100110 01101111 01101111
    所以，如果执行 setbit('n1', 7, 1)，则就会将第7位设置为1，
        那么最终二进制则变成 01100111 01101111 01101111，即："goo"
 
# 扩展，转换二进制表示：
 
    # source = "苑辰奇"
    source = "foo"
 
    for i in source:
        num = ord(i)
        print bin(num).replace('b','')
 
    特别的，如果source是汉字 "苑辰奇"怎么办？
    答：对于utf-8，每一个汉字占 3 个字节，那么 "苑辰奇" 则有 9个字节
       对于汉字，for循环时候会按照 字节 迭代，那么在迭代时，将每一个字节转换 十进制数，然后再将十进制数转换成二进制
```



getbit(name, offset)

```
# 获取name对应的值的二进制表示中的某位的值 （0或1）
```

bitcount(key, start=None, end=None)

```
# 获取name对应的值的二进制表示中 1 的个数
# 参数：
    # key，Redis的name
    # start，位起始位置
    # end，位结束位置
```

bitop(operation, dest, *keys)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 获取多个值，并将值做位运算，将最后的结果保存至新的name对应的值
 
# 参数：
    # operation,AND（并） 、 OR（或） 、 NOT（非） 、 XOR（异或）
    # dest, 新的Redis的name
    # *keys,要查找的Redis的name
 
# 如：
    bitop("AND", 'new_name', 'n1', 'n2', 'n3')
    # 获取Redis中n1,n2,n3对应的值，然后讲所有的值做位运算（求并集），然后将结果保存 new_name 对应的值中
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

strlen(name)

```
# 返回name对应值的字节长度（一个汉字3个字节）
```

incr(self, name, amount=1)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。
 
# 参数：
    # name,Redis的name
    # amount,自增数（必须是整数）
 
# 注：同incrby
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

incrbyfloat(self, name, amount=1.0)

```
# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。
 
# 参数：
    # name,Redis的name
    # amount,自增数（浮点型）
```

decr(self, name, amount=1)

```
# 自减 name对应的值，当name不存在时，则创建name＝amount，否则，则自减。
 
# 参数：
    # name,Redis的name
    # amount,自减数（整数）
```

append(key, value)

```
# 在redis name对应的值后面追加内容
 
# 参数：
    key, redis的name
    value, 要追加的字符串
```



#### 其他常用操作

delete(*names)

```
# 根据删除redis中的任意数据类型
```

exists(name)

```
# 检测redis的name是否存在
```

keys(pattern='*')

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 根据模型获取redis的name
 
# 更多：
    # KEYS * 匹配数据库中所有 key 。
    # KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
    # KEYS h*llo 匹配 hllo 和 heeeeello 等。
    # KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

expire(name ,time)

```
# 为某个redis的某个name设置超时时间
```

rename(src, dst)

```
# 对redis的name重命名为
```

move(name, db))

```
# 将redis的某个值移动到指定的db下
```

randomkey()

```
# 随机获取一个redis的name（不删除）
```

 type(name)

```
# 获取name对应值的类型
```

scan(cursor=0, match=None, count=None)
scan_iter(match=None, count=None)

```
# 同字符串操作，用于增量迭代获取key
```
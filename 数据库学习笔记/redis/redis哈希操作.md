



Hash操作，redis中Hash在内存中的存储格式如下图：

![![hash](file:///C:/Users/Avalon/Desktop/Django/%E5%A4%8D%E4%B9%A0/redis/img/hash.png?lastModify=1511296565)](./img/hash.png)



hset(name, key, value)



```
# name对应的hash中设置一个键值(这里的值是一个字典对象)对（不存在，则创建；否则，修改）
 
# 参数：
    # name，redis的name
    # key，name对应的hash中的key
    # value，name对应的hash中的value
 
# 注：
    # hsetnx(name, key, value),当name对应的hash中不存在当前key时则创建（相当于添加）
```



hmset(name, mapping)

hmset(name, mapping)

```
# 在name对应的hash中批量设置键值对
 
# 参数：
    # name，redis的name
    # mapping，字典，如：{'k1':'v1', 'k2': 'v2'}
 
# 如：
    # r.hmset('xx', {'k1':'v1', 'k2': 'v2'})
```



hget(name,key)

```
# 在name对应的hash中获取根据key获取value
```

hmget(name, keys, *args)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 在name对应的hash中获取多个key的值
 
# 参数：
    # name，reids对应的name
    # keys，要获取key集合，如：['k1', 'k2', 'k3']
    # *args，要获取的key，如：k1,k2,k3
 
# 如：
    # r.mget('xx', ['k1', 'k2'])
    # 或
    # print r.hmget('xx', 'k1', 'k2')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

hgetall(name)

```
#获取name对应hash的所有键值
```

hlen(name)

```
# 获取name对应的hash中键值对的个数
```

hkeys(name)

```
# 获取name对应的hash中所有的key的值
```

hvals(name)

```
# 获取name对应的hash中所有的value的值
```

hexists(name, key)

```
# 检查name对应的hash是否存在当前传入的key
```

hdel(name,*keys)

```
# 将name对应的hash中指定key的键值对删除
```



hincrby(name, key, amount=1)

```
# 自增name对应的hash中的指定key的值，不存在则创建key=amount
# 参数：
    # name，redis中的name
    # key， hash对应的key
    # amount，自增数（整数）
```

hincrbyfloat(name, key, amount=1.0)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 自增name对应的hash中的指定key的值，不存在则创建key=amount
 
# 参数：
    # name，redis中的name
    # key， hash对应的key
    # amount，自增数（浮点数）
 
# 自增name对应的hash中的指定key的值，不存在则创建key=amount
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

hscan(name, cursor=0, match=None, count=None)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆
 
# 参数：
    # name，redis的name
    # cursor，游标（基于游标分批取获取数据）
    # match，匹配指定key，默认None 表示所有的key
    # count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
 
# 如：
    # 第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
    # 第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
    # ...
    # 直到返回值cursor的值为0时，表示数据已经通过分片获取完毕
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

hscan_iter(name, match=None, count=None)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 利用yield封装hscan创建生成器，实现分批去redis中获取数据
 
# 参数：
    # match，匹配指定key，默认None 表示所有的key
    # count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
 
# 如：
    # for item in r.hscan_iter('xx'):
    #     print item
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)


```
有序集合，在集合的基础上，为每元素排序；元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数(权重)，分数专门用来做排序。
```

zadd(name, *args, **kwargs)

```
# 在name对应的有序集合中添加元素
# 如：
     # zadd('zz', 'n1', 1, 'n2', 2)
     # 或
     # zadd('zz', n1=11, n2=22)
```

zcard(name)

```
# 获取name对应的有序集合元素的数量
```

zcount(name, min, max)

```
# 获取name对应的有序集合中分数 在 [min,max] 之间的个数
```

zincrby(name, value, amount)

```
# 自增name对应的有序集合的 name 对应的分数
```

r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 按照索引范围获取name对应的有序集合的元素
 
# 参数：
    # name，redis的name
    # start，有序集合索引起始位置（非分数）
    # end，有序集合索引结束位置（非分数）
    # desc，排序规则，默认按照分数从小到大排序
    # withscores，是否获取元素的分数，默认只获取元素的值
    # score_cast_func，对分数进行数据转换的函数
 
# 更多：
    # 从大到小排序
    # zrevrange(name, start, end, withscores=False, score_cast_func=float)
 
    # 按照分数范围获取name对应的有序集合的元素
    # zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
    # 从大到小排序
    # zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

zrank(name, value)

```
# 获取某个值在 name对应的有序集合中的排行（从 0 开始）
 
# 更多：
    # zrevrank(name, value)，从大到小排序
```

zrangebylex(name, min, max, start=None, num=None)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 当有序集合的所有成员都具有相同的分值时，有序集合的元素会根据成员的 值 （lexicographical ordering）来进行排序，而这个命令则可以返回给定的有序集合键 key 中， 元素的值介于 min 和 max 之间的成员
# 对集合中的每个成员进行逐个字节的对比（byte-by-byte compare）， 并按照从低到高的顺序， 返回排序后的集合成员。 如果两个字符串有一部分内容是相同的话， 那么命令会认为较长的字符串比较短的字符串要大
 
# 参数：
    # name，redis的name
    # min，左区间（值）。 + 表示正无限； - 表示负无限； ( 表示开区间； [ 则表示闭区间
    # min，右区间（值）
    # start，对结果进行分片处理，索引位置
    # num，对结果进行分片处理，索引后面的num个元素
 
# 如：
    # ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
    # r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']
 
# 更多：
    # 从大到小排序
    # zrevrangebylex(name, max, min, start=None, num=None)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

zrem(name, values)

```
# 删除name对应的有序集合中值是values的成员
 
# 如：zrem('zz', ['s1', 's2'])
```

zremrangebyrank(name, min, max)

```
# 根据排行范围删除
```

zremrangebyscore(name, min, max)

```
# 根据分数范围删除
```

zremrangebylex(name, min, max)

```
# 根据值返回删除
```

zscore(name, value)

```
# 获取name对应有序集合中 value 对应的分数
```

zinterstore(dest, keys, aggregate=None)

```
# 获取两个有序集合的交集，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为:  SUM  MIN  MAX
```

zunionstore(dest, keys, aggregate=None)

```
# 获取两个有序集合的并集，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为:  SUM  MIN  MAX
```

zscan(name, cursor=0, match=None, count=None, score_cast_func=float)
zscan_iter(name, match=None, count=None,score_cast_func=float)

```
# 同字符串相似，相较于字符串新增score_cast_func，用来对分数进行操作
```
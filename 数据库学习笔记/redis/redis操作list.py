import redis

r = redis.Redis()

# 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
# 如：
# r.lpush('oo', 11,22,33)
# 保存顺序为: 先33,再22,最后11
# lpush(name,values)
r.lpush('avalon',1,2,3)
#
print(r.llen('avalon'))

# r.lrem(name, value, num)
# 在name对应的list中删除指定的值

# 参数：
# name，redis的name
# value，要删除的值
# num，  num=0，删除列表中所有的指定值；
# num=2,从前到后，删除2个；
# num=-2,从后向前，删除2个
# r.lrem('avalon',1,num=2)

#lpop(name)
# 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
print(r.lpop('avalon')) # 获得不到东西就返回None


# lindex(name, index)
print(r.lindex('avalon',0))
#在name对应的列表中根据索引获取列表元素

# lrange(name, start, end)

# 在name对应的列表分片获取数据
# 参数：
    # name，redis的name
    # start，索引的起始位置
    # end，索引结束位置
print(r.lrange('avalon',0,r.llen('avalon')))
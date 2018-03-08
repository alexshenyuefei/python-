import redis
r = redis.Redis()

r.hset('fate','saber','亚瑟王')

r.hmset('fate',{'archer':'卫宫士郎','caster':'梅林','saber':'两仪式'})

print(r.hget('fate','archer').decode())

"""
下面获取会返回一个列表,两者是等价的.
"""
print(r.hmget('fate','archer','caster'))
print(r.hmget('fate',['archer','caster']))

#获取name对应hash的所有键值
print(r.hgetall('fate')) # 返回字典类型
print(r.hlen('fate')) # 字典长度
print(r.hkeys('fate')) # 字典中所有key的值,返回列表
print(r.hvals('fate')) # 字典中所有value的值,返回列表
print(r.hexists('fate','saber')) # 检查name对应的hash是否存在当前传入的key

r.hdel('fate','saber') # 将name对应的hash中指定key的键值对删除
print(r.hgetall('fate'))


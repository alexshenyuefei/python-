import redis
r = redis.Redis()

r.sadd('ubw',1,2,3,4,5) # 添加重复值没效果
print(r.scard('ubw'))
# 把5元素从ubw集合中拿走
print(r.srem('ubw','5')) #成功就返回1
print(r.srem('ubw','123')) #没删除成功就返回0
print('-'*10)
print(r.sismember('ubw',2))

# 获取name对应的集合的所有成员
a = r.smembers('ubw')
print(a,type(a)) # 类型也是set
print(r.spop('ubw'))

# 从集合的右侧（尾部）移除一个成员，并将其返回
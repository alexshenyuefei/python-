import redis


r = redis.Redis()
r.set('foo', 'Bar')
a = r.get('foo')
print(a,type(a)) #返回的都是bytes类型
r.set('saber','阿尔托利亚')
print(r.get('saber').decode())
# 只有name不存在时，执行设置操作（添加）
r.setnx('saber','亚瑟王')
print(r.get('saber').decode())
# 有效时间设置为1秒
r.set('archer','卫宫士郎',px=1)
print(r.get('archer',))
# 这两种方法都行
r.mset({'k1': 'v1', 'k2': 'v2'})
r.mset(k1='v1', k2='v2')

"""
get方法
"""
print(r.get('k1'))
# 返回列表
print(r.mget('k1','k2')) # [b'v1', b'v2']
#设置新值并获取原来的值
print(r.getset('k1', 'newk1'))
print(r.get('k1'))


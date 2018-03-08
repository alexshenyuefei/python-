import redis

r = redis.Redis()

r.zadd('fatezero','n1',1,'n2',2)

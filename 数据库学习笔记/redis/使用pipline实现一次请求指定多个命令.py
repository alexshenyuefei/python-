import redis

pool = redis.ConnectionPool()

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

r.set('name', 'alex')
r.set('role', 'acc')


pipe.execute()
print(r.get('name'))
print(r.get('role'))
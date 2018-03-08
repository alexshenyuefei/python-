# 关于列表的增量迭代
# 由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：
    # 1、获取name对应的所有列表
    # 2、循环列表
# 但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：
import redis
r = redis.Redis()
r.lpush('avalon',1,2,3)


def list_iter(name):
    list_count = r.llen(name)
    for index in range(list_count):
        yield r.lindex(name,index)


for item in list_iter('avalon'):
    print(item)
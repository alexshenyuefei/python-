### 发布订阅

![订阅](./img/dingyue.png)



发布者：服务器

订阅者：Dashboad和数据处理

Demo如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='10.211.55.4')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

订阅者：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from monitor.RedisHelper import RedisHelper
 
obj = RedisHelper()
redis_sub = obj.subscribe()
 
while True:
    msg= redis_sub.parse_response()
    print msg
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

发布者：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from monitor.RedisHelper import RedisHelper
 
obj = RedisHelper()
obj.public('hello')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

更多参见：https://github.com/andymccurdy/redis-py/

http://doc.redisfans.com/
在项目的setting.py中设置

```python
DOWNLOADER_MIDDLEWARES = {
    'WandoujiaCrawler.middlewares.ProxyMiddleware': 100,
}
```

其中WandoujiaCrawler是我们的项目名称,后面的数字代表中间件执行的优先级,官方文档中默认proxy中间件的优先级编号是750,我们的中间件优先级要高于默认的proxy中间键.中间件middlewares.py的写法如下(scrapy默认会在这个文件中写好一个中间件的模板,不用管它写在后面即可):

middlewares.py

```
# -*- coding: utf-8 -*-
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://proxy.yourproxy:8001"
```



这里有两个问题: 
一是proxy一定是要写号http://前缀的否则会出现**to_bytes must receive a unicode, str or bytes object, got NoneType**的错误. 
二是官方文档中写到process_request方法一定要返回**request对象,response对象或None**的一种,但是其实写的时候不用return,乱写可能会报错. 
另外如果代理有用户名密码等就需要在后面再加上一些内容:

```
# Use the following lines if your proxy requires authentication
proxy_user_pass = "USERNAME:PASSWORD"
# setup basic authentication for the proxy
encoded_user_pass = base64.encodestring(proxy_user_pass)
request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
```

```python
# 有密码的代理配置参考
# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64 
# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
  
        # Use the following lines if your proxy requires authentication
        proxy_user_pass = "USERNAME:PASSWORD"
        # setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
```


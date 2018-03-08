"""
https://p.3.cn/prices/mgets?&skuIds=J_11757834
内容:[{"op":"62.80","m":"93.00","id":"J_11757834","p":"62.80"}]
"""
import requests
import json
URL = 'https://p.3.cn/prices/mgets?&skuIds=J_11757834'
r = requests.get(url=URL,)
print(type(r.content),r.content.decode())
content = json.loads(r.content)
print(type(content),content)
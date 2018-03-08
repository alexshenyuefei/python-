# pprint模块需要安装
import pprint
import json

with open('豆瓣美剧.json','r',encoding='utf-8') as f:
    # pprint.pprint(f.read()) 注意pprint只能打印python数据格式
    # print(f.read())
    content = f.read()
    pprint(json.loads(content))
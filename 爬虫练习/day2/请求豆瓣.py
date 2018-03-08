import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}  # 模拟浏览器的请求头部
URL = r'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1509358965499'
america_Url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios1&start=0&count=18'
r = requests.get(url=URL, headers=headers)
h = requests.get(url=america_Url, headers=headers)
content = r.content.decode()  # 默认返回str格式的json数据
content2 = h.content.decode()  # 默认返回str格式的json数据
content = json.loads(content)  # 转化成python格式
content2 = json.loads(content2)  # 转化成python格式
with open('豆瓣国产剧.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(content, ensure_ascii=False, indent=2))  # json格式转化关闭ascii转化,2个缩进,写入文件

with open('豆瓣美剧.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(content2, ensure_ascii=False, indent=2))  # json格式转化关闭ascii转化,2个缩进,写入文件

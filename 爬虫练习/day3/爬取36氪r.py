import requests
import re

content = ""
URL = 'http://36kr.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}

response = requests.get(url=URL,headers=headers,timeout=3)
"""
36氪是一堆js脚本动态生成的html样式,爬虫没有渲染功能无法执行js,
使用正则表达式提取数据
"title":"雷蛇拟香港IPO，创始人有望一跃成为亿万富豪"
"summary":"游戏行业正在增长，市场增长潜力更大。"
"title":"每日投融资速递 | 小猪短租获得1.2亿美元融资, Kymera Therapeutics获得3000万美元融资 ——2017.11.1"
"summary":"今日共有30起融资事件"

小猪短租获得1.2亿美元融资, Kymera Therapeutics获得3000万美元融资 ——2017.11.1",
"catch_title":"",
"summary":"今日共有30起融资事件",
"""
"""
,"catch_title":"",
"""
"""
import re
result = re.findall(r'(a)(b)(c)','abcabcaabb')
print(result)
实验结果
[('a', 'b', 'c'), ('a', 'b', 'c')]
多个括号结果是元组
"""
p = re.compile(r'"title":"(.*?)".*?"summary":"(.*?)"',re.S)
result = p.findall(response.content.decode(), re.S)
print(result)
for i in result:
    """('股权投资项目', '“能落地，少花钱，别流产”')"""
    content += '新闻标题: '+i[0]+'\n'+'新闻简介: '+i[1]+'\n\n'
with open('36氪第一页新闻.txt','w',encoding='utf-8')as f:
    f.write(content)
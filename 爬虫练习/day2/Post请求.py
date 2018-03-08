import requests
import json
# from:zh
# to:en
# query:生活
# transtype:translang
# simple_means_flag:3
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}  # 模拟浏览器的请求头部
data = {"from": 'zh', 'to': 'en', 'query': '生活', 'transtype': 'translang', 'simple_means_flag': '3'}
r = requests.post('http://fanyi.baidu.com/v2transapi', data=data, headers=headers)
results_dict = json.loads(r.content.decode())
result = results_dict['trans_result']['data'][0]['dst']
print(data['query'], '翻译结果是', result)

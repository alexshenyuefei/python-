import requests
import re
import pprint
URL='http://neihanshequ.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    ,'Cookie': 'csrftoken=a8f94fae114add4f0573423efce42cb2; tt_webid=6482985907326567949; uuid="w:2d50ade59e914ffaa92439d250eadd32"; _ga=GA1.2.1319713786.1509437836; _gid=GA1.2.857297505.1509437836; _gat=1'
    }

resopnse = requests.get(url=URL,headers=headers)

print(resopnse.status_code)
index_strs = resopnse.content.decode()
# print(index_strs)
"""
<p>昨晚在酒吧，邂逅一位半老徐娘。虽然57岁，但她依旧风韵犹存，我们推杯换盏、打情骂俏了一会儿，她用迷离的眼神看着我，问我有没有试过母女双飞。我说没有。我们又喝了一会儿酒，她说，今晚算你走运了哦。于是她领着我去她家。她进门，打开灯，对着楼上喊了一句：</p>
"""
index_strs_pipei = re.findall(r'<p>(.*?)</p>',index_strs,re.S)

pprint.pprint(index_strs_pipei)

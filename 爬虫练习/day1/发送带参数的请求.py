import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'} #模拟浏览器的请求头部
# parms={'wd':'python'}
parms=dict(wd='python')
# url='https://www.baidu.com/s?wd='
r = requests.get('http://www.baidu.com/s?',params=parms,headers=headers)

print(r.status_code)  # 查看请求状态
print(r.request.url)  # 查看请求的url
print(r.url)  # 查看响应的url


import requests
# 米扑代理
proxies ={'http':'http://89.218.188.4:3128'}
r = requests.get('https://www.baidu.com/',proxies=proxies)
print(r.status_code)

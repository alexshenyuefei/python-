import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'} #模拟浏览器的请求头部

r = requests.get('http://www.sina.com',headers=headers)
# print(r.text)
print(r.content.decode())
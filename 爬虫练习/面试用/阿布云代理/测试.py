import requests
import proxies
from threading import Thread



URL= 'https://www.lagou.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3112.113 Safari/537.36',
           "Referer": "https://www.lagou.com/jobs/list_python"}
while True:
    a = requests.get(url=URL, headers=headers, proxies=proxies.getproxies())
    # a = requests.get(url=URL, headers=headers,)
    print(a.content.decode())
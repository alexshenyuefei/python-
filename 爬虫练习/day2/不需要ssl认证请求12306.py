import requests

response = requests.get("https://www.12306.cn/mormhweb/ ", verify=False,timeout=3,)  # 超时参数3秒
print(response.status_code)

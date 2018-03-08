# requsets 发送网络请求,返回响应数据
import requests
# 添加请求头内的参数
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'} #模拟浏览器的请求头部

r = requests.get('http://www.baidu.com',headers=headers)
print(r.text) # 根据requsets猜测的编码方式,进行内容解码
r.encoding='utf-8'
r.content.decode()
r.headers # 响应头
r.request.headers # 请求头
print(r.request.headers) # 请求头


baidu_logo ='https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png'
h = requests.get(baidu_logo)
with open('baidu.png','wb') as f:
    f.write(h.content)





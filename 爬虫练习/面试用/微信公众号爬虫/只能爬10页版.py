import requests
import pymongo
from urllib.parse import urlencode

from lxml.etree import XMLSyntaxError
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq

client=pymongo.MongoClient('localhost')
db = client['LDC']


keyword = 'LDC法式甜点  '

base_url = 'http://weixin.sogou.com/weixin?'
proxies = {'http': 'http://HR774417JL9RN37D:97E8FE87DE7E3196@http-dyn.abuyun.com:9020',
           'https': 'http://HR774417JL9RN37D:97E8FE87DE7E3196@http-dyn.abuyun.com:9020'}

headers={
    # 'Cookie':'SUID=D5B7136E3921940A00000000596989A2; SUV=00E050A46E13B7D5596989A3B0E37685; usid=lNnciQvnJQLAa5UT; ld=Gyllllllll2zxKLulllllVIjt37lllllNQSu7kllll9lllllpklll5@@@@@@@@@@; LSTMV=380%2C26; LCLKINT=1015; ABTEST=0|1514545198|v1; weixinIndexVisited=1; JSESSIONID=aaalcCEe4p336h4RXOw8v; IPLOC=CN1100; sct=4; PHPSESSID=96vt03bugso5ooncq7q8osavf5; SUIR=1FDD9BFAD7D2B7979C611C74D7BCDD47; SNUID=E4937BFB8C89ECF7E33ADD9E8DE81325; seccodeRight=success; successCount=1|Fri, 29 Dec 2017 13:20:56 GMT; ppinf=5|1514553446|1515763046|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo3OlJpY2FyZG98Y3J0OjEwOjE1MTQ1NTM0NDZ8cmVmbmljazo3OlJpY2FyZG98dXNlcmlkOjQ0Om85dDJsdURWYzVpR2JPWXlFdVhHVGFyRHhiZkVAd2VpeGluLnNvaHUuY29tfA; pprdig=GEkgNHHv4SJT1dd0jM6ttg16Db2kjbvoRfjmaokDqksg3mNeGPWOu5D8WNveis4h-8CHURL7-kfpefGTvlODZd3j0WqpBwf5QQEty84Dh1Oyu9mnWde_ZaAXQ5qKNDbbNjH5b5esZ35iNKbaepnVVu6GvWoRHEG0aU0VnD9arQs; sgid=16-32717015-AVpGQGb7VGlo0eR33ZqgsQU; ppmdig=15145534460000001b6dffdafcb45910681f20655887ffd1',
    'Host':'weixin.sogou.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}


def get_html(url):
    try:
        # response = requests.get(url=url,allow_redirects=False,headers=headers,proxies=proxies)  #不让自动处理跳转
        session = requests.session()
        response = session.get(url=url,allow_redirects=False,headers=headers,proxies=proxies)  #不让自动处理跳转
        if response.status_code==200:
            return response.text
        if response.status_code==302:
            # ip被封
            print('302')
            get_html(url)
    except ConnectionError:
        print('ConnectionError')
        get_html(url)



def get_index(keyword,page):
    data = {
        'query':keyword,
        'type':2,#请求文章
        'page':page
    }
    queries = urlencode(data)
    url = base_url+queries
    html = get_html(url)
    return html


def parse_index(html): #获得微信搜索页上文章连接
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items() #返回一个生成器
    for item in items:
        yield item.attr('href')


def get_detail(url): #获取微信文章详情,没有反爬
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html): #解析详情
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text() #文章
        content = doc('.rich_media_content').text() #内容
        data = doc('#post-date').text() # 日期
        nickname = doc('#js_profile_qrcode > div > strong').text() #作者
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text() # 公众号
        return {
            'title':title,
            'content':content,
            'data':data,
            'nickname':nickname,
            'wechat':wechat,
        }
    except XMLSyntaxError:
        return None


def save_to_mongo(data):
    # 文章标题重复则不插入,更新杰克
    # 第一个参数是查询基准点,{'$set':data}把键值声明为set,Data表示如果查询到结果是已经有的就更新,没有的就插入
    if db['artilces'].update({'title':data['title']},{'$set':data},True):
        print('Save to Mongo',data['title'])
    else:
        print('Save to Mongo Failed',data['title'])

def main():
    for i in range(1,11):
        print('*'*10,'第',i,'页')
        html = get_index(keyword,i)
        if html:
            article_urls = parse_index(html) # 这里变量是一个生成器对象
            for article_url in article_urls:
                # print(article_url) #打印列表页链接
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    # print(article_data)
                    if article_data:
                        save_to_mongo(article_data)
        else:
            print(html)
if __name__ == '__main__':
    main()
import requests
from lxml import etree

URL='https://www.qiushibaike.com/8hr/page/{}/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


class QiushiSpider(object):
    def __init__(self):
        self.url = URL
        self.headers = headers


    def get_urllists(self):
        url_lists = []
        for i in range(13):
            url_lists.append(self.url.format(i+1))
        return url_lists

    def parse_url(self,url):
        response = requests.get(url=url,headers=self.headers)
        temp_html = etree.HTML(response.content.decode())
        html_elements_lists = temp_html.xpath(r"//div[contains(@class,'article')]")
        """
        父元素 ://div[contains(@class,'article')]
        """


if __name__ == '__main__':
    r = QiushiSpider()
    print(r.get_urllists())
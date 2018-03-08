import requests
from lxml import etree
import os



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
URL = 'https://book.douban.com/top250?start={}'
content = ""
"""
大的图书元素 ://tr[@class='item']
书名://tr[@class='item']//a/text() 或者说父元素的.//a/text()
作者和出版社信息://tr[@class='item']//p/text() 
评分://tr[@class='item']//span[@class='rating_nums']/text()
简介//tr[@class='item']//p/span
图片地址://tr[@class='item']//a[@class='nbg']/img/@src
"""
def douban_book_list():
    global content
    for i in range(9):
        response = requests.get(url=URL.format(i*25),headers=headers)
        temp_html = etree.HTML(response.content.decode())
        book_element_list = temp_html.xpath(r"//tr[@class='item']")
        book_lists = []
        for book_element in book_element_list:
            book = {}
            book['title'] = book_element.xpath(r'.//a[@title]/text()') if len(book_element.xpath('.//a/text()'))>0 else None
            book['writer'] = book_element.xpath(r".//p/text()") if len(book_element.xpath(".//p/text()")) > 0 else None
            book['score'] = book_element.xpath(r".//span[@class='rating_nums']/text()") if len(book_element.xpath(".//span[@class='rating_nums']/text()")) >0 else None
            book['brief'] = book_element.xpath(r".//p/span/text()") if len(book_element.xpath(r".//p/span/text()")) >0 else ["",]
            book['img_url'] = book_element.xpath(r".//a[@class='nbg']/img/@src") if len(book_element.xpath(".//a[@class='nbg']/img/@src")) >0 else None
            book_lists.append(book)
        print(book_lists)
        """
        book_lists
        [{'title': ['\n              ', '\n            ', '\n                追风筝的人\n\n                \n              '], 
        'writer': ['[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元', '\n                  ', '\n              '], 
        'score': ['8.9'], 'brief ': ['为你，千千万万遍'],
         'img_url': ['https://img3.doubanio.com/mpic/s1727290.jpg']},
        """
        for book in book_lists:
            content += '书名: ' + book['title'][0].strip()+'\n'
            content += '作者: ' + book['writer'][0]+'\n'
            content += '评分: ' + book['score'][0]+'\n'
            content += '简介: ' + book['brief'][0]+'\n'+'\n'
            # content += '图片地址' + book['img_url'][0]+'\n'+'\n'
            book_image = requests.get(url=book['img_url'][0],headers=headers)
            with open('图书图片/{}.jpg'.format(book['title'][0].strip()),'wb') as f:
                f.write(book_image.content)
    with open('豆瓣图书.txt','w',encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    try:
        os.mkdir('图书图片')
    except FileExistsError:
        print('文件夹已经存在')
    douban_book_list()
from lxml import etree
import requests
import os
"""
第一页:https://movie.douban.com/top250?start=0
第二页:https://movie.douban.com/top250?start=25
"""

content = ""
movie_num = 0

#1:从url地址获取response请求
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
URL = 'https://movie.douban.com/top250?start={}'

def douban_movie_250():
    for i in range(10):
        response = requests.get(url=URL.format(i*25),headers=headers)
        #2:将response请求通过etree转化
        temp_html = etree.HTML(response.content.decode())
        # print(etree.tostring(temp_html).decode())  #查看经过etree处理后的html到底是什么样子的
        #3:通过xpath取到资源
        """
        
        //div[@class='item']//div[@class='hd']//span[@class='title']
        肖申克的救赎
         / The Shawshank Redemption
        霸王别姬
        这个杀手不太冷
         / Léon
        阿甘正传
         / Forrest Gump
        
        
        
        """
        movie_title = temp_html.xpath(r"//div[@class='item']//div[@class='hd']//span[@class='title'][1]/text()")
        # print(movie_title[0])  #打印选取到的资源
        movie_pingfen = temp_html.xpath(r'//*[@property="v:average"]/text()')
        movie_image=temp_html.xpath(r'//a/img[@src]/@src')

        #组合数据
        # movies = [[movie_title[0],movie_pingfen[0],movie_image]]
        movies = []
        for i in range(25):
            movie=[]
            global movie_num
            movie_num += 1
            movie.append('排名{} :'.format(movie_num)+movie_title[i])
            movie.append('\n'+'评分 '+movie_pingfen[i])
            movie.append('\n'+'图片地址: '+movie_image[i]+'\n\n')
            movies.append(movie)

        for movie in movies:
            global content
            content += movie[0]+movie[1]+movie[2]

        # 根据图片地址保存图片
        for i in range(25):
            image_requset = requests.get(url=movie_image[i])
            with open('电影图片/{}.jpg'.format(movie_title[i]), 'wb') as f:
                f.write(image_requset.content)

#4:保存
if __name__ == '__main__':
    try:
        os.mkdir('电影图片')
    except FileExistsError:
        print('文件夹已经存在')
    douban_movie_250()
    with open('豆瓣电影.txt','a',encoding='utf-8') as f:
        f.write(content)
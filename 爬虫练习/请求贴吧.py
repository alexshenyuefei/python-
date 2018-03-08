import os
import requests
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TiebaSpider(object):
    def __init__(self, tieba_name):
        self.url_temp = 'http://tieba.baidu.com/f?kw='+tieba_name+'&pn={}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}  # 模拟浏览器的请求头部
        self.headers=headers
        self.tieba_name = tieba_name
        # 当前目录下创建文件夹
        now_dir_path = os.path.dirname(os.path.abspath(__file__))
        try:
            os.mkdir(now_dir_path + '\\贴吧{}'.format(self.tieba_name))
        except FileExistsError:
            print("文件夹已经存在")


    # 1,url list
    def get_url_list(self):
        urllist = []
        for i in range(20):
            url = self.url_temp.format(i*50)
            urllist.append(url)
        return urllist

    def send_get(self,urls):
        # r = requests.get('http://tieba.baidu.com/f?',params=parms,headers=headers)
        r = requests.get(url=urls,headers=self.headers)
        return r

    def save_files_(self,r,count):
        with open('贴吧{}\\贴吧{}第{}页.html'.format(self.tieba_name, self.tieba_name, count), 'w', encoding='utf-8') as f:
            content = r.content.decode()
            f.write(content)

    def run(self):# 实现我们的主要逻辑
        url_lists = self.get_url_list()
        count = 1
        for url in url_lists:
            #2, 发送请求,获取响应
            r = self.send_get(url)
            self.save_files_(r,count)
            count += 1


if __name__ == '__main__':
    tieba_sprider = TiebaSpider('织部里沙')
    tieba_sprider.run()
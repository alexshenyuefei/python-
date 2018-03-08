"""
通过微博的高级搜索,搜索关键字的微博
"""
import logging
import urllib.parse
import requests
import time
import weibologin
from lxml import etree
import sys
import xlwt
import xlrd

class SearchWeiboDate(object):
    def __init__(self,keyword,startTime,endTime,interval='50',flag=True, begin_url_per = "http://s.weibo.com/weibo/"):
        """
        :param keyword:
        :param startTime:
        :param interval:
        :param flag:
        :param begin_url_per:
        """
        self.begin_url_per = begin_url_per  # 设置固定地址部分，默认为"http://s.weibo.com/weibo/"
        self.setKeyword(keyword)  # 设置关键字
        self.setStartTimescope(startTime,endTime)
        self.setInterval(interval)  # 设置邻近网页请求之间的基础时间间隔（注意：过于频繁会被认为是机器人）
        self.setFlag(flag)  # 设置是否被反爬抓到,若为False，需要进入页面，手动输入验证码
        self.logger = logging.getLogger(__name__)  # 初始化日志
        login = weibologin.WeiboLogin('17610766215', 'kongzhijingjie')
        time.sleep(4)
        self.login_session = login.login()


    def setKeyword(self, keyword):
        """keyword两次utf8 urlencode编码"""
        self.keyword = urllib.parse.quote(keyword)  # 先将其GBK解码，然后再UTF-8编码，然后再输出：
        self.keyword = urllib.parse.quote(self.keyword)

    def setStartTimescope(self, startTime,endTime):
        """
        从2017年11月10日0点搜到2017年11月24日0点
        2017-11-10-0:2017-11-24-0
        将self.timescope设置成 2017-11-10-0:2017-11-24-0
        :param startTime: 2017-11-10-0这样的格式0表示0点,15点写成-15
        :param endTime:2017-11-24-0
        :return:
        """
        self.timescope = startTime+":"+endTime


    ##设置邻近网页请求之间的基础时间间隔
    def setInterval(self, interval):
        self.interval = int(interval)

    ##设置是否被认为机器人的标志。若为False，需要进入页面，手动输入验证码
    def setFlag(self, flag):
        self.flag = flag

    def getURL(self):
        url = self.begin_url_per+self.keyword+"&typeall=1&suball=1"
        url += "&timescope=custom:"+self.timescope+"&page="
        return url

    ##爬取一次请求中的所有网页，最多返回50页
    def download(self, url, maxTryNum=4):
        hasMore = True  #某次请求可能少于50页，设置标记，判断是否还有下一页
        isCaught = False    #某次请求被认为是机器人，设置标记，判断是否被抓住。抓住后，需要复制log中的文件，进入页面，输入验证码
        i = 1  # 记录本次请求所返回的页数
        while hasMore and i < 51 and (not isCaught):    #最多返回50页，对每页进行解析，并写入结果文件
            source_url = url + str(i)  # 构建某页的URL  在原来的基础上加上page后面的页码
            data = ''   #存储该页的网页数据
            time.sleep(4)
            html = self.login_session.get(source_url, timeout=12,headers=weibologin.HEADERS)
            data = html.content.decode()
            lines = data.splitlines()  #按照行分隔，返回一个包含各行作为元素的列表
            isCaught = True
            for line in lines:
                if line.startswith(
                        '<script>STK && STK.pageletM && STK.pageletM.view({"pid":"pl_weibo_direct"'):  ##判断字符串以   开头，此处是微博页面代码
                    """

                    """
                    isCaught = False  # 没被反爬虫屏蔽
                    n = line.find('html":"')  ##返回html在该行的索引值
                    """
                    "html":"开头下面内容是
                    <div class=\"S_content clearfix\">\n <div class=\"S_content_l\">\n  <div id=\"pl_common_pinyinerr\"><\/div>\n  <div id=\"pl_weibo_shareres\"><\/div>\n  <div id=\"pl_weibo_directtop\" smartconf=\"type=1\" class=\"clearfix\" node-type=\"like\"><\/div>\n <div id=\"pl_weibo_filter
                    这些html标签了
                    """

                    if n > 0:
                        print("-" * 15)
                        j = line[n + 7: -12].encode("utf-8").decode('unicode_escape').replace("\\", "")
                        print(j)

                        if (j.find('<div class="search_noresult">') > 0):
                            ## 没有更多结果页面 这一页没结果
                            hasMore = False
                        else:
                            page = etree.HTML(j)
                            ps1 = page.xpath("//p[@node-type='feed_list_content']")  # 使用xpath解析得到微博内容
                            as2 = page.xpath("//a[@class='W_texta W_fb']")  # 使用xpath解析得到博主地址
                            ai = 0
                            # 获取昵称和微博内容
                            for p1 in ps1:
                                name = p1.attrib.get('nick-name')
                                txt = p1.xpath('string(.)')
                                addr1 = as2[ai].attrib.get('href')
                                u = addr1.find('u/')
                                addr = ''
                                if u > 0:
                                    addr = addr1.replace("u/", "p/100505") + '/info?mod=pedit_more'
                                else:
                                    addr = addr1 + '/info?mod=pedit_more'  # 获得博主个人信息地址
                                print("name",name)
                                print("txt",txt)
                                print("addr1",addr1)
                                print("addr",addr)


def main_():
    logger = logging.getLogger('main')  #获得日志系统的  对象，即创建一个logger
    logFile = './collect.log'
    logger.setLevel(logging.DEBUG)      #设置日志级别 NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
    filehandler = logging.FileHandler(logFile)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)


    keyword = input('Enter the keyword(type \'quit\' to exit ):')
    if keyword == 'quit':
        sys.exit()
    spider = SearchWeiboDate(keyword=keyword,startTime='2017-11-10-0',endTime='2017-11-24-0')
    url = spider.getURL()
    print(url)
    spider.download(url)

if __name__ == '__main__':
    main_()


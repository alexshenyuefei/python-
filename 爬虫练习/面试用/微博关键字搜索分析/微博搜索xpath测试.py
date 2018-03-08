import weibologin
import requests
import time
from lxml import etree
import proxies


def get_haixin_html():
    url = "http://s.weibo.com/weibo/%25E6%25B5%25B7%25E4%25BF%25A1&typeall=1&suball=1&timescope=custom:2017-11-11-0:2017-11-19-0&page=1"

    login = weibologin.WeiboLogin('17610766215', 'kongzhijingjie')
    login_session = login.login()
    # print(a, type(a))
    time.sleep(3)
    search_response = login_session.get(url=url, headers=weibologin.HEADERS,proxies=proxies.getproxies())
    # with open("haixin.html", 'w', encoding='utf-8') as f:
    #     f.write(search_response.content.decode())
    return search_response.content.decode()


def get_content_list(html_str):
    html = etree.HTML(html_str)
    # print(html)
    ps1 = html.xpath("//p[@node-type='feed_list_content']")
    print(ps1)
    as2 = html.xpath("//a[@class='W_texta W_fb']")  # 使用xpath解析得到博主地址
    ai = 0
    item = {}
    for p1 in ps1:
        item["name"] = p1.attrib.get('nick-name')
        item["txt"] = p1.xpath('string(.)')
        item["addr1"] = as2[ai].attrib.get('href')
        print(item)


if __name__ == '__main__':
    html_str = get_haixin_html()

    # with open("./haixin.html", 'r', encoding='utf-8') as f:
    #     html_str = f.read()
    lines = html_str.splitlines()
    for line in lines:
        if line.startswith(r'<script>STK && STK.pageletM && STK.pageletM.view({"pid":"pl_weibo_direct"'):  ##判断字符串以   开头，此处是微博页面代码
            isCaught = False # 没被反爬虫屏蔽
            n = line.find('html":"')  ##返回html在该行的索引值
            """
            "html":"开头下面内容是
            <div class=\"S_content clearfix\">\n <div class=\"S_content_l\">\n  <div id=\"pl_common_pinyinerr\"><\/div>\n  <div id=\"pl_weibo_shareres\"><\/div>\n  <div id=\"pl_weibo_directtop\" smartconf=\"type=1\" class=\"clearfix\" node-type=\"like\"><\/div>\n <div id=\"pl_weibo_filter
            这些html标签了
            """

            # print("/"*16)
            # print(n)
            # print("/" * 16)

            if n > 0:
                # print("-" * 15)
                j = line[n + 7: -12].encode("utf-8").decode('unicode_escape').replace("\\", "")
                # print(j)
                # print("-"*15)
                with open('lines.html', 'w', encoding="utf-8") as f:
                    for i in j:
                        f.write(i)
                        # f.write('\n')

                if (j.find('<div class="search_noresult">') > 0):
                    ## 没有更多结果页面 这一页没结果
                    hasMore = False
                else:
                    page = etree.HTML(j)
                    ps1 = page.xpath("//p[@node-type='feed_list_content']")  # 使用xpath解析得到微博内容
                    as2 = page.xpath("//a[@class='W_texta W_fb']")  # 使用xpath解析得到博主地址
                    ai = 0
                    # print("*"*10)
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




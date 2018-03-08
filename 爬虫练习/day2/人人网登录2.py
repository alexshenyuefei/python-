# coding=utf-8
import requests
import re

post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }

headers['cookie']='anonymid=j5tv65p7-3sboh2; jebe_key=ef8751d2-7a42-4b08-bb15-f34dbf807647%7Ccfcd208495d565ef66e7dff9f98764da%7C1507309057034%7C0; __utma=151146938.303604063.1507309058.1507309058.1507309058.1; __utmz=151146938.1507309058.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; depovince=BJ; _r01_=1; _ga=GA1.2.303604063.1507309058; _gid=GA1.2.738372020.1509352486; JSESSIONID=abcOEJE-2JCWP_ohBEU9v; jebecookies=654e7850-6574-440a-aeb9-065c4b6c47a1|||||; ick_login=0db617e3-f64d-40dd-a2db-5d5d31e22faa; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=fa4cc459fb7d4bc7829118203b1be05a9; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20171010/1615/main_MnPP_c975000084fe1986.jpg; t=78fe0ac28df0b24f3ab09585d4a7223a9; societyguester=78fe0ac28df0b24f3ab09585d4a7223a9; id=327550029; xnsid=916f930d; loginfrom=syshome; ch_id=10016; wp_fold=0'
"""
人人网这个登录的cookie要在登录成功之后的页面去找响应拿cookie
人人网的登录不需要发送post请求之后才能登录,只要找登录后的cookie设置抓取cookie值,设置cookie就表示已经登录
"""

# h=requests.post(url=post_url,data=post_data,headers=headers)
# print('毛兆军' in h.content.decode())

#请求个人主页
r = requests.get("http://www.renren.com/327550029/profile",headers=headers)

#判断是否登陆成功
print(re.findall("毛兆军",r.content.decode()))

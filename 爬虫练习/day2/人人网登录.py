# coding=utf-8
import requests
import re

session = requests.session()  #实例化一个session,这里是会话的意思,可复用,意思是post请求之后还能get
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
"""
人人网的登录是一个form表单,使用post请求键值对提交表单
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

session.post(post_url,data=post_data,headers=headers)

#使用保存有cookies的session进行后续的操作
#请求个人主页
r = session.get("http://www.renren.com/327550029/profile",headers=headers)

#判断是否登陆成功
print(re.findall("毛兆军",r.content.decode()))
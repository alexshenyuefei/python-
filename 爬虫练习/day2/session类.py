"""
requests 提供了一个叫做session类，来实现客户端和服务端的会话保持
session = requests.session()
response = session.get(url,headers)
"""
import requests
re = requests.session()

"""
Session类对象自动保存cookie.
"""
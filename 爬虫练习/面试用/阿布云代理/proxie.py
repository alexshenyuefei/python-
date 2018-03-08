"""
使用之前登录:https://www.abuyun.com/官网
注册账号,充值使用http动态版隧道
将通行证书,通行密钥填入proxyUser,proxyPass
"""
import requests

proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "HR774417JL9RN37D"
proxyPass = "97E8FE87DE7E3196"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

def getproxies():
    return proxies

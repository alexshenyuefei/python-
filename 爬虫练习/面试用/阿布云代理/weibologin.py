import requests
import re
import base64
import rsa
import binascii
import proxie

print("avalon")

# LOGIN_URL='https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}
postdata = {
    'entry': 'weibo',
    'gateway': '1',
    'from': '',
    'savestate': '7',
    'userticket': '1',
    'ssosimplelogin': '1',
    'vsnf': '1',
    'vsnval': '',
    'su': '',
    'service': 'miniblog',
    'servertime': '',
    'nonce': '',
    'pwencode': 'rsa2',  # 加密算法
    'sp': '',
    'encoding': 'UTF-8',
    'prelt': '401',
    'rsakv': '',
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    'returntype': 'META'
}


class WeiboLogin(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def prelog(self):
        """登录前获取数据"""
        prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su={}&rsakt=mod&client=ssologin.js(v1.4.19)'.format(self.username)
        r = requests.get(url=prelogin_url, headers=HEADERS)
        """
        返回数据是sinaSSOController.preloginCallBack(...)
        message会匹配到以下字符串
        {"retcode":0,"servertime":1511536526,"pcid":"gz-639da2147717459fc090c55b8f1053b7d96e","nonce":"XG3S5H","pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443","rsakv":"1330428213","uid":"6408715506","exectime":5}
        """
        p = re.compile(r'\((.*?)\)')
        message = p.search(r.content.decode()).group(1)
        message = eval(message) # 将字符串转化为字典
        self.pubkey = str(message.get('pubkey'))
        self.servertime = str(message.get('servertime'))
        self.nonce = str(message.get('nonce'))
        self.rsakv = str(message.get('rsakv'))

    def update_postdate(self):
        """生成要提交的表单数据"""
        global postdata
        postdata['servertime'] = self.servertime
        postdata['nonce'] = self.nonce
        postdata['su'] = self.encrypt_username()
        postdata['sp'] = self.encrypt_password()
        postdata['rsakv'] = self.rsakv

    def encrypt_username(self):
        """生成加密的用户名"""
        username = self.username
        username = base64.b64encode(username.encode())
        return username


    def encrypt_password(self):
        """生成加密的密码"""
        rsa_pub_key = int(self.pubkey,16) # 16进制转换
        key = rsa.PublicKey(rsa_pub_key,65537) #创建公钥
        message = self.servertime + '\t' + self.nonce + '\n' + self.password# 密码和别的一起组合
        password = rsa.encrypt(message.encode(), key)  # 加密
        password = binascii.b2a_hex(password)  # 将加密信息转换为16进制。
        return password

    def login(self):
        session = requests.Session()
        url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
        try:
            self.prelog()
        except Exception as e:
            print(e)
            print("prelog方法出错")
            return
        self.update_postdate()
        r = session.post(url=url,headers = HEADERS,data=postdata)
        """
        返回相应响应含有
        location.replace('http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack&di');
        """
        p = re.compile(r'location\.replace\(\'(.*?)\'\)')
        text = r.content.decode('GBK')
        try:
            login_url = p.search(text).group(1)
            respr = session.get(url=login_url,headers = HEADERS,proxies=proxie.getproxies())
            # print(respr.text)
            uid = re.findall('"uniqueid":"(\d+)",',respr.content.decode('GBK'))[0]
            # url = "http://weibo.com/u/" + uid # 个人原创微博首页
            url = "http://weibo.com/u/" + uid+"/home" # 个人微博首页
            resp = session.get(url,headers = HEADERS)
            # print(resp.content.decode())
            # print(resp.cookies)
            print("登录成功")
            return session
        except Exception as e:
            print(e)
            print("登录不成功")





if __name__ == '__main__':
    login = WeiboLogin('17610766215','kongzhijingjie')
    a = login.login()
    print(a,type(a))




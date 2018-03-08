"""
自己写的请求url地址的方法,请求头中user-agent分为电脑和手机两种
"""
import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def parse_url_pc(url):
    headers_pc = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    r = requests.get(url=url,headers = headers_pc,timeout = 3)
    assert r.status_code == 200
    return r

def parse_url_mobile(url):
    headers_mobile = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    r = requests.get(url=url,headers = headers_mobile,timeout = 3)
    assert r.status_code == 200
    return r


if __name__ == '__main__':
    response = parse_url_mobile('http://www.baidu.com')
    print(response.content.decode())
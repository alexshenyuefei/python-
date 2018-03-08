# -*- coding: cp936 -*-
import os
import time
from ctypes import *
import requests
YDMApi = windll.LoadLibrary('yundamaAPI-x64') #64位系统要调用64位的

# 云打码平台用户账号及其密码,非开发者账号
username = b'avalonfate'

password = b'avalonfate1234'



def yanzm(filename):
    appId = 4326  # 软件IＤ，开发者分成必要参数。
    appKey = b'f687d5cc2a8fd52d38549913421859d6'  # 软件密钥，开发者分成必要参数。
    # 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。
    # 在此查询所有类型 http://www.yundama.com/price.html
    """
    5000	不定长汉字英文数字、符号、空格	
    """
    codetype = 5000
    result = c_char_p(b"                              ")  # 分配30个字节存放识别结果
    timeout = 30  # 识别超时时间 单位：秒

    # 一键识别函数，无需调用 YDM_SetAppInfo 和 YDM_Login，适合脚本调用
    # 错误代码请查询 http://www.yundama.com/apidoc/YDM_ErrorCode.html
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    # print("一键识别：验证码ID：%d，识别结果：%s" % (captchaId, result.value))
    # print(type(result.value))
    # result.value是bytes,decode转换成str(unicode)类型

    # captchaId 不知道干吗用
    # return captchaId, result.value.decode()

    return result.value.decode()
if __name__ == '__main__':
    # 默认从当前文件夹找起
    # for index, file in enumerate(os.listdir('data')):
    #     filename = b'data/%s' % file.encode()
    #     print(filename)
    #     # result = yanzm(filename)
    #     # print(index,filename,"结果是",result)
    # 验证码图片网址
    response = requests.get(url='https://login.sina.com.cn/cgi/pin.php?r=97440740&amp;s=0&amp;p=gz-6b0796ce09c47c60293e76f0551646a4d99b')
    with open('yanzm.png','wb') as f:
        f.write(response.content)
    filename = b'yanzm.png'
    result = yanzm(filename)
    print(filename, "结果是", result)
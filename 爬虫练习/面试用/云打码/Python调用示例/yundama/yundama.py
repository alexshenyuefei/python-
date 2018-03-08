# -*- coding: cp936 -*-
import os
import time
from ctypes import *
YDMApi = windll.LoadLibrary('yundamaAPI')

# 云打码平台用户账号及其密码
username = 'avalonfate'
password = 'avalonfate1234'



def yanzm(filename):
    appId = 4326  # 软件Ｄ，开发者分成必要参数。
    appKey = 'f687d5cc2a8fd52d38549913421859d6'  # 软件密钥，开发者分成必要参数。
    # 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。
    # 在此查询所有类型 http://www.yundama.com/price.html
    """
    5000	不定长汉字英文数字、符号、空格	
    """
    codetype = 5000
    result = c_char_p("                              ")  # 分配30个字节存放识别结果
    timeout = 30  # 识别超时时间 单位：秒

    # 一键识别函数，无需调用 YDM_SetAppInfo 和 YDM_Login，适合脚本调用
    # 错误代码请查询 http://www.yundama.com/apidoc/YDM_ErrorCode.html
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    print(result)
    return captchaId, str(result)[10: -2]

if __name__ == '__main__':
    path_=os.path.dirname(__file__)
    print(path_)
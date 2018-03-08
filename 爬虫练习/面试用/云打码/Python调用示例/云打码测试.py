# -*- coding: cp936 -*-

import os
import time
from ctypes import *
YDMApi = windll.LoadLibrary('yundamaAPI')

# 云打码平台用户账号及其密码
username = 'xxxxxx'
password = 'xxxxxx'

def getVertify(filename):
    '''
    识别验证码
    :param filename: 验证码路径
    :return: 识别的验证码
    '''

    appId = 2976   # 软件Ｄ，开发者分成必要参数。
    appKey = 'b66d5f677b6a44f38cdff116215890d8'  # 软件密钥，开发者分成必要参数。

    # 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。
    # 在此查询所有类型 http://www.yundama.com/price.html
    codetype = 5000
    result = c_char_p("                              ")  # 分配30个字节存放识别结果
    timeout = 60  # 识别超时时间 单位：秒

    # 一键识别函数，无需调用 YDM_SetAppInfo 和 YDM_Login，适合脚本调用
    # 错误代码请查询 http://www.yundama.com/apidoc/YDM_ErrorCode.html
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)

    return captchaId, str(result)[10: -2]

def main():
    '''
    测试主体函数
    :return:
    '''

    for index, file in enumerate(os.listdir('data')):
        filename = 'data/%s' % file
        result = getVertify(filename)
        open('result.txt', 'a').write('%s\t%s\t%s\n' % (filename, result[0], result[1]))
        print 'The %d %s is finished!' % (index, result[0])

    balance = YDMApi.YDM_GetBalance(username, password)
    print u'登陆成功，用户名：%s，剩余题分：%d' % (username, balance)


if __name__ == '__main__':

    BeginTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'Begin:' + BeginTime
    main()
    EndTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'Begin:%s\nEnd:%s' % (BeginTime, EndTime)
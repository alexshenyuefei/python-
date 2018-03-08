# -*- coding: cp936 -*-

import os
import time
from ctypes import *
YDMApi = windll.LoadLibrary('yundamaAPI')

# �ƴ���ƽ̨�û��˺ż�������
username = 'xxxxxx'
password = 'xxxxxx'

def getVertify(filename):
    '''
    ʶ����֤��
    :param filename: ��֤��·��
    :return: ʶ�����֤��
    '''

    appId = 2976   # ����ģ������߷ֳɱ�Ҫ������
    appKey = 'b66d5f677b6a44f38cdff116215890d8'  # �����Կ�������߷ֳɱ�Ҫ������

    # ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ�
    # �ڴ˲�ѯ�������� http://www.yundama.com/price.html
    codetype = 5000
    result = c_char_p("                              ")  # ����30���ֽڴ��ʶ����
    timeout = 60  # ʶ��ʱʱ�� ��λ����

    # һ��ʶ������������� YDM_SetAppInfo �� YDM_Login���ʺϽű�����
    # ����������ѯ http://www.yundama.com/apidoc/YDM_ErrorCode.html
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)

    return captchaId, str(result)[10: -2]

def main():
    '''
    �������庯��
    :return:
    '''

    for index, file in enumerate(os.listdir('data')):
        filename = 'data/%s' % file
        result = getVertify(filename)
        open('result.txt', 'a').write('%s\t%s\t%s\n' % (filename, result[0], result[1]))
        print 'The %d %s is finished!' % (index, result[0])

    balance = YDMApi.YDM_GetBalance(username, password)
    print u'��½�ɹ����û�����%s��ʣ����֣�%d' % (username, balance)


if __name__ == '__main__':

    BeginTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'Begin:' + BeginTime
    main()
    EndTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'Begin:%s\nEnd:%s' % (BeginTime, EndTime)
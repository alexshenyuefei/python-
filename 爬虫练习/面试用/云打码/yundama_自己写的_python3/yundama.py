# -*- coding: cp936 -*-
import os
import time
from ctypes import *
import requests
YDMApi = windll.LoadLibrary('yundamaAPI-x64') #64λϵͳҪ����64λ��

# �ƴ���ƽ̨�û��˺ż�������,�ǿ������˺�
username = b'avalonfate'

password = b'avalonfate1234'



def yanzm(filename):
    appId = 4326  # ���I�ģ������߷ֳɱ�Ҫ������
    appKey = b'f687d5cc2a8fd52d38549913421859d6'  # �����Կ�������߷ֳɱ�Ҫ������
    # ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ�
    # �ڴ˲�ѯ�������� http://www.yundama.com/price.html
    """
    5000	����������Ӣ�����֡����š��ո�	
    """
    codetype = 5000
    result = c_char_p(b"                              ")  # ����30���ֽڴ��ʶ����
    timeout = 30  # ʶ��ʱʱ�� ��λ����

    # һ��ʶ������������� YDM_SetAppInfo �� YDM_Login���ʺϽű�����
    # ����������ѯ http://www.yundama.com/apidoc/YDM_ErrorCode.html
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    # print("һ��ʶ����֤��ID��%d��ʶ������%s" % (captchaId, result.value))
    # print(type(result.value))
    # result.value��bytes,decodeת����str(unicode)����

    # captchaId ��֪��������
    # return captchaId, result.value.decode()

    return result.value.decode()
if __name__ == '__main__':
    # Ĭ�ϴӵ�ǰ�ļ�������
    # for index, file in enumerate(os.listdir('data')):
    #     filename = b'data/%s' % file.encode()
    #     print(filename)
    #     # result = yanzm(filename)
    #     # print(index,filename,"�����",result)
    # ��֤��ͼƬ��ַ
    response = requests.get(url='https://login.sina.com.cn/cgi/pin.php?r=97440740&amp;s=0&amp;p=gz-6b0796ce09c47c60293e76f0551646a4d99b')
    with open('yanzm.png','wb') as f:
        f.write(response.content)
    filename = b'yanzm.png'
    result = yanzm(filename)
    print(filename, "�����", result)
# -*- coding: cp936 -*-
import os
import time
from ctypes import *
YDMApi = windll.LoadLibrary('yundamaAPI')

# �ƴ���ƽ̨�û��˺ż�������
username = 'avalonfate'
password = 'avalonfate1234'



def yanzm(filename):
    appId = 4326  # ����ģ������߷ֳɱ�Ҫ������
    appKey = 'f687d5cc2a8fd52d38549913421859d6'  # �����Կ�������߷ֳɱ�Ҫ������
    # ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ�
    # �ڴ˲�ѯ�������� http://www.yundama.com/price.html
    """
    5000	����������Ӣ�����֡����š��ո�	
    """
    codetype = 5000
    result = c_char_p("                              ")  # ����30���ֽڴ��ʶ����
    timeout = 30  # ʶ��ʱʱ�� ��λ����

    # һ��ʶ������������� YDM_SetAppInfo �� YDM_Login���ʺϽű�����
    # ����������ѯ http://www.yundama.com/apidoc/YDM_ErrorCode.html
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    print(result)
    return captchaId, str(result)[10: -2]

if __name__ == '__main__':
    path_=os.path.dirname(__file__)
    print(path_)
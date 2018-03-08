from yundama import yanzm
import os

for file in os.listdir('data'): #查找当前目录下data下的文件名
    filename = b'data/%s' % file.encode('cp936')
    # print(filename)
    result = yanzm(filename)
    print(filename,'验证码是',result)
    # print(index, filename, "结果是", result)
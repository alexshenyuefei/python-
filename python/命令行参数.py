# sys模块通过sys.argv提供对命令行参数的访问,命令行参数是调用某个程序时,除程序名外的其他参数
# 切换到文件所在目录,python 命令行参数.py 1,2,3,4
import sys
print('你输入参数长度是',len(sys.argv))
print('这些参数是',str(sys.argv))
print(sys.argv[0])
# sys.argv是一个列表,第0项是文件名,第一项是命令行之后跟的第一个参数
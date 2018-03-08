"""
windows的换行是\r\n，unix的是\n，mac的是\r。
因为不同系统下默认的换行符不同。字符处理时候，这样的“不同”会带来很大的问题
"""
"""
Python 2（PEP 278 -- Universal Newline Support）：
1）如果不是txt文件，建议用wb和rb来读写。通过二进制读写，不会有换行问题。
2）如果需要明文内容，请用rU来读取（强烈推荐），即U通用换行模式（Universal new line mode）。该模式会把所有的换行符（\r \n \r\n）替换为\n。只支持读入，但是也足够了。这是Python 提供给我们的最好的选择，没有之一。对比r和rU的结果：
content = file(fn, 'r').read()
test\r\ntest2
这里的换行会因不同系统而不同
content = file(fn, 'rU').read()
test\ntest2
所有的换行都被统一，不分系统
"""
"""
python建议使用wb,rb读写数据
"""
"""
with open('阿瓦隆','wb') as f: # 此处没有encoding='utf-8',二进制读写没有编码指定
    f.write('阿尔托利亚'.encode())
    f.write('\n'.encode())
    f.write('阿瓦隆'.encode())
"""
"""
rb读出的不是明文数据
"""
with open('阿瓦隆','rb') as f:
    print(f.read())
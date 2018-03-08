# UnicodeDecodeError: 'gbk',比如爬淘宝登录页,网页charset基于gbk
# 爬虫时候经常出现
"""
目标网站程序员的锅，将其他编码的字符串比如utf-8或者shift-jis或者big5之类的直接拼了进来。
"""

# 在decode的时候指定错误处理方式：
"""
my_str.decode('gbk', 'ignore')
"""
"""
有strict, ignore和replace三种处理方式，
strict是默认的也就是抛出异常，ignore是忽略非法字符，
replace是在这里加一个非法字符的unicode标记。encode也有相同的参数。
"""

strs = u'abc中国'.encode('gbk') + u'dsae非法字符asfe$#@@'.encode('utf-8')
strs.decode('gbk','ignore')
print(strs.decode('gbk','ignore'))
print(strs.decode('gbk','replace')) # replace会加非法字符标记

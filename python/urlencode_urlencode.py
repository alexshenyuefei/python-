"""
http://s.weibo.com/weibo/%25E6%25B5%25B7%25E4%25BF%25A1&Refer=index
"""
a ="%25E6%25B5%25B7%25E4%25BF%25A1"
import urllib.parse
"""
键值对urlencode
目前不提供urldecode方法
"""
values={}
values['username']='02蔡彩虹'
values['password']='ddddd?'
data=urllib.parse.urlencode(values)
print(data)
"""
字符串urlencode
"""
data="海信"
date2 = urllib.parse.quote(data)
print(date2)
date3 = urllib.parse.quote(date2)
print(date3)

"""
字符串urldecode
"""
print("*"*10)
print(urllib.parse.unquote(date2))
unquote1 = urllib.parse.unquote(date3)
unquote2 = urllib.parse.unquote(unquote1)
print(unquote2)

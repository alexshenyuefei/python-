import re

"""
match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：
match从字符串的一开始匹配起
"""
print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))

# 切分字符串
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[a-d]+','123a1234abc123456'))

# 提取子串,用()表示的就是要提取的分组（Group）

"""
^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
"""
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

print(m.group(0)) # '010-12345'group()默认是group 0

print(m.group(1)) # 010
print(m.group(2)) # 12345

"""
注意到group(0)永远是原始字符串，
group(1)、group(2)……表示第1、2、……个子串。

"""
"""
正则识别合理时间
groups输出所有匹配的子串,没有()使用groups没意义
"""
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

"""
search则不是从头开始匹配,默认一个个找string中符合的正则表达式
"""
print("*"*8)
m2 = re.search(r'(\d{3})-(\d{3,8})$', 'aa010-12345')
print(m2.group())


"""编译正则表达式,提高速度"""
test2 = re.compile(r'\d{3}-\d{3}-\d{4}')
result = test2.match('123-456-7890')
print(result.group())

test2 = re.compile(r'(\d{3}|\(\d{3}\))-\d{3}-\d{4}')
result1 = test2.match('(123-456-7890')
result2 = test2.match('123)-456-7890')
result3 = test2.match('123-456-7890')
result4 = test2.match('(123)-456-7890')


print(result1,result2,result4)
print(result3,)


""""
re.findall方法
搜索string，以列表形式返回全部能匹配的子串。
"""
p = re.compile(r'\d+')
print(p.findall('one1two2three3four4'))
str1 = "this is string example....wow!!!"
"""
只要是可迭代对象都可以用sorted
"""

#sorted(itrearble, key=None, reverse=False)
"""
itrearble:可迭代对象
key:选择要作为排序依据的关键字,每次送入可迭代对象每次迭代元素作为输入变量
reverse=False 升序
reverse=True 降序
不写默认是升序
"""

l = [('b',2),('a',1),('c',3),('d',4)]
print(sorted(l,key=lambda x:x[1],reverse=True))
print(sorted(l,key=lambda x:x[1],reverse=False))
print(sorted(l,key=lambda x:x[1]))

alist = ['123', 'abc', 'xyz', 'xyz', 'zara']
alist.sort()
print(alist)
blist = ['123', 'a1bc', 'xyz', 'xyz', 'zara']
print(sorted(blist,key=lambda x:x[2])) #用第二个字母排序
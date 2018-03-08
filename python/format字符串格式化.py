# 通过{}和%来代替传统%
# 1、使用位置参数
name = ['LiSA', 30]
strings = 'my name is {},age{}.'.format('LiSA', 30)
print(strings)
strings = 'my name is {0},age{1},hello,{0}.'.format('LiSA', 30)
print(strings)
strings = 'my name is {},age{}.'.format(*name)
print(strings)


# 2使用关键字参数,关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可
hashes=dict(name='LiSA',age=30)
strings = 'my name is {age},age{name}.'.format(**hashes)
print(strings)
strings = 'my name is {name},age{age}.'.format(name='LiSA',age=30)
print(strings)

# 3、填充与格式化
print('{0:*>10}'.format(10))  # 右对齐
print('{0:*<10}'.format(10))  # 左对齐
print('{0:*^10}'.format(10))  # 居中对齐

# 4、精度与进制

print('{0:.2f}'.format(1/3))  # 精确到小数点后两位
print('{0:b}'.format(10))  # 10的2进制数
print('{0:o}'.format(10))  # 10的八进制
print('{0:x}'.format(10))  # 16进制
'{:,}'.format(12369132698)  #千分位格式化

# 5、使用索引
name = ['LiSA', 30]
print('name is {1[0]},age is {1[1]}'.format('avalon',name))
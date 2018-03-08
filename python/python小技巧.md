

遍历列表输出索引

```python
array = [1, 2, 3, 4, 5]

for i in range(len(array)):
    print (i, array[i])
    
# Pythonic 
for i, item in enumerate(array):
    print (i, item)
```



对列表的操作

```python
array = [1, 2, 3, 4, 5]

new_array = []
for item in array:
    new_array.append(str(item))

# Pythonic
new_array = [str(item) for item in array]

# Generator
new_array = (str(item) for item in array)

# 函数式
new_array = map(str, array)
```



列表推导

```python
# 生成列表
[ i*i for i in range(10) if i % 2 == 0 ]
# 生成集合
{ i*i for i in range(10) if i % 2 == 0 }
# 生成字典
{ i:i for i in range(10) if i % 2 == 0 }
```



上下文管理器

```python
file = open('file', 'w')
file.write(123)
file.close()

# Pythonic
with open('file', 'w') as file:
    file.write(123)
```



条件判断

```python
if x is True:
    y = 1
else:
    y = -1

# Pythonic
y = 1 if x is True else -1
```



变量交换

```
temp = y
y = x
x = temp

# Pythonic
x, y = y, x
```



列表反转

```python
array = [1, 2, 3, 4, 5]

l = len(array)
for i in range(l/2):
    temp = array[l - i - 1]
    array[l - i - 1] = array[i]
    array[i] = temp

array = list(reversed(array))
# Pythonic
array = array[::-1]
```



读取文件

```
CHUNK_SIZE = 1024

with open('test.json') as f:
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        if chunk:
            print(chunk)
        chunk = f.read(CHUNK_SIZE)

from functools import partial
# Pythonic
with open('test.json') as f:
    for piece in iter(partial(f.read, CHUNK_SIZE), ''):
        print (piece)
# Lambda
with open('test.json') as f:
    for piece in iter(lambda: f.read(CHUNK_SIZE), ''):
        print (piece)
```





for-else和try-else语法

```
is_for_finished = True

try:
    for item in array:
        print (item)
        # raise Exception
except:
    is_for_finished = False

if is_for_finished is True:
    print ('complete')
    
# Pythonic
for item in array:
    print (item)
    # raise Exception
else:
    print ('complete')

try:
    print ('try')
    # raise Exception
except Exception:
    print ('exception')
else:
    print ('complete')
```





函数参数解压

```python
def draw_point(x, y):
    # do some magic

point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

draw_point(*point_foo)
draw_point(**point_bar)
```



列表/元组解压

```python
first, second, *rest = (1,2,3,4,5,6,7,8)
first:1
second:2
rest:[3,4,5,6,7,8]
```



"Print To"语法

```python
# 2.x
print >>  open("myfile", "w"), "hello world"
# 3.x
print ("hello world", file=open("myfile", "w"))
```



字典缺省值

```python
d = {}

try:
    d['count'] = d['count'] + 1
except KeyError:
    d['count'] = 0
# Pythonic
d['count'] = d.get('count', 0) + 1
```



链式比较符

```python
if x < 100 and x > 0:
    print(x)
# Pythonic
if 0 < x < 100:
    print(x)
```





多行字符串

```python
s = ("longlongstringiii"
    "iiiiiiiii"
    "iiiiiii")

print(s)
```



in表达式

```python
if 'string'.find('ring') > 0:
    print ('find')
# Pythonic
if 'ring' in 'string':
    print ('find')

for r in ['ring', 'ring1', 'ring2']:
    if r == 'ring':
        print ('find')
# Pythonic
if 'ring' in ['ring', 'ring1', 'ring2']:
    print('find')
```



字符串连接

```python
array = ['a', 'b', 'c', 'd', 'e']
s = array[0]
for char in array[1:]:
    s += ',' + char
# Pythonic
s = ','.join(array)
```



列表合并字典

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]

d = {}
for key, value in zip(keys, values):
    d[key] = value
# Better
d = dict(zip(keys, values))
# Pythonic
d = {key: value for key, value in zip(keys, values)}
```



all和any

```python
# Pythonic
#可迭代对象conditions中有一个的bool值为假,则flag为假
flag = all(conditions)
#可迭代对象conditions中有一个的bool值为真,则flag为真
flag = any(conditions)

```



开启本地目录的HTTP服务器

```
python2 -m SimpleHTTPServer 8080 # 2.x
python3 -m http.server 8080 # 3.x
```



在Python使用花括号块

```
from __future__ import braces
```



Python之禅

```
import this
```


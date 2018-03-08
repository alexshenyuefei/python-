import json
from pprint import pprint

# 1:json.dumps
# json.dumps 用于将 Python 对象编码成 JSON 字符串。
data = dict(a='a', b='b', c='c')
data_json = json.dumps(data) # 将python数据格式转化为Json数据格式

# 2:json.loads
data_ = json.loads(data_json)  # 将Json数据格式转化为Python数据格式

# 3:序列化和反序列化
# 在python中，序列化可以理解为：把python的对象编码转换为json格式的字符串，
# 反序列化可以理解为：把json格式字符串解码为python数据对象。
# 在python的标准库中，专门提供了json库与pickle库来处理这部分。
print(json.__all__) # 查看Json库所有方法
data = {'name' : '亚瑟王','address':'阿瓦隆'}
print('序列化后的数据',json.dumps(data))

# 在dumps函数中添加参数ensure_ascii=False
print('ensure_ascii=False,序列化后的数据',json.dumps(data,ensure_ascii=False))

# indent 是缩进
# ensure_ascii=False 用于保存中文
s = json.dumps(data, indent=2, ensure_ascii=False)

# 将json文件反序列化:
# 两步操作：1、先读取文件的json字符串对象；2、然后反序列化成python数据结构
with open('豆瓣美剧.json','r',encoding='utf-8') as f:
    content = f.read()
    pprint(content)
    pprint(json.loads(content)) # 转化成Python数据格式打印

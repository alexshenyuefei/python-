from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
# 本地时间是指当前操作系统设定的时区
print(datetime.utcfromtimestamp(t)) # UTC时间
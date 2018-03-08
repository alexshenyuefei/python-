# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0
# （1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00  是0时区的时间
# timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了
from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20)
print(dt.timestamp())

# Python的timestamp是一个浮点数
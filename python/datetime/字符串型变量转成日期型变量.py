# 字符串与time类型的转换
import time
import datetime
timestr = "time2009-12-14"
t = time.strptime(timestr, "time%Y-%m-%d")
print(t)
print(t.tm_year)
create_time = "2017-11-06 23:54:10"
t2 = time.strptime(create_time,"%Y-%m-%d %H:%M:%S")
print(t2)
"""
下面是格式化符号汇总

　　%a 星期几的简写 Weekday name, abbr.
　　%A 星期几的全称 Weekday name, full
　　%b 月分的简写 Month name, abbr.
　　%B 月份的全称 Month name, full
　　%c 标准的日期的时间串 Complete date and time representation
　　%d 十进制表示的每月的第几天 Day of the month
　　%H 24小时制的小时 Hour (24-hour clock)
　　%I 12小时制的小时 Hour (12-hour clock)
　　%j 十进制表示的每年的第几天 Day of the year
　　%m 十进制表示的月份 Month number
　　%M 十时制表示的分钟数 Minute number
　　%S 十进制的秒数 Second number
　　%U 第年的第几周，把星期日做为第一天（值从0到53）Week number (Sunday first weekday)
　　%w 十进制表示的星期几（值从0到6，星期天为0）weekday number
　　%W 每年的第几周，把星期一做为第一天（值从0到53） Week number (Monday first weekday)
　　%x 标准的日期串 Complete date representation (e.g. 13/01/08)
　　%X 标准的时间串 Complete time representation (e.g. 17:02:10)
　　%y 不带世纪的十进制年份（值从0到99）Year number within century
　　%Y 带世纪部分的十制年份 Year number
　　%z，%Z 时区名称，如果不能得到时区名称则返回空字符。Name of time zone
　　%% 百分号
"""

# 2: time类型与datetime类型的转换
d = datetime.datetime(* t2[:6])
print(type(d),d)

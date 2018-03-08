# pip install fake-useragent 第一次运行时候需要翻墙获取user-agent
from fake_useragent import UserAgent
import random
ua = UserAgent()
UA_LISTS = [ua.random for i in range(10)]
print(UA_LISTS)

#随机选择一个user-agent
print(random.choice(UA_LISTS))
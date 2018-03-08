from datetime import datetime
now = datetime.now()
dt = datetime(2015, 4, 19, 12, 20)
print(now.strftime('%a, %b %d %H:%M'))
print(dt.strftime('%a, %b %d %H:%M'))

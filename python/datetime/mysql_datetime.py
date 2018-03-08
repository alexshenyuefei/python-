from datetime import date, datetime, timedelta
import pymysql
import time
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'python',
          'db':'test',
          'charset':'utf8'
          }

connection = pymysql.connect(**config)


# 获取明天的时间
tomorrow = datetime.now().date() + timedelta(days=1)
create_time = "2017-11-06 23:54:10"

t2 = time.strptime(create_time,"%Y-%m-%d %H:%M:%S")
d = datetime(* t2[:6])

try:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO times(times) VALUES (%s)'
        cursor.execute(sql, (tomorrow,))
        cursor.execute(sql, (date(1989, 6, 14),))
        cursor.execute(sql, (d,))
    connection.commit()
except Exception:
    pass
finally:
    connection.close()
from pymysql import *

conn = connect(host='localhost', port=3306,
                       database='work', user='root',
                       password='python', charset='utf8')
cs1 = conn.cursor()
cs1.execute('SELECT position_id FROM pythonshanghai')
result = cs1.fetchall()
# print(result)
for i in result:
    print(i[0])
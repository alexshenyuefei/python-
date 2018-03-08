import pymysql
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'python',
          'db':'test',
          'charset':'utf8'
          }

connection = pymysql.connect(**config)

def date_insert():
    with connection.cursor() as cursor:
        sql = 'INSERT INTO test_(id,name,num) VALUES (%s,%s,%s);'
        cursor.execute(sql, (6,'Lisa',6))
    connection.commit()
if __name__ == '__main__':
    date_insert()
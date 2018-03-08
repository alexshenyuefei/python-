from pymysql import *

if __name__ == "__main__":
    try:
        conn = connect(host='localhost', port=3306,
                       database='test', user='root',
                       password='python', charset='utf8')
        cs1 = conn.cursor()
        cs1.execute('SELECT * FROM customers')
        result = cs1.fetchall()
        for i in result:
            print(i)
    except Exception as e:
        print(e)
    finally:
        cs1.close()

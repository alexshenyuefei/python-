from pymysql import *
from redis import *
from hashlib import sha1

def mysql_login():
    try:
        connec_=connect(host='localhost', user='root', password='python', database='test',
                       port=3306, charset='utf8')
        cs = connec_.cursor()
        sql = 'SELECT * FROM userlist WHERE user_name = %s'
        result = cs.execute(sql, username)
        if result==0:
            print('用户名不存在')
        else:
            result = cs.fetchone()
            mysql_pwd = result[2]
            if mysql_pwd == password:
                print('登录成功')
                sr.set(username,password)
            else:
                print('密码错误登录失败')
        cs.close()
    except Exception as e:
        print(e)
    finally:
        connec_.close()


if __name__ == '__main__':
    username = input('请输入用户名:')
    password = input('请输入密码:')

    sh = sha1()
    sh.update(password.encode())
    password = sh.hexdigest()

    sr = StrictRedis(decode_responses = True)
    res = sr.get(username)
    # print(res)
    if res is None:
        mysql_login()
    else:
        if res == password:
            print('redis登录成功')
        else:
            print('redis登录失败')

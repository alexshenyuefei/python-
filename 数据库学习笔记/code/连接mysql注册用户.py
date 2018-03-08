from pymysql import *
from hashlib import sha1


if __name__ == '__main__':
    username = input("请输入用户名")
    password = input("请输入密码")

    #密码加密
    sh = sha1()
    sh.update(password.encode())
    password = sh.hexdigest()
    try:
        connec = connect(host='localhost', port=3306,
                           database='test', user='root',
                           password='python', charset='utf8')
        cs1=connec.cursor()
        result = cs1.execute('SELECT * FROM userlist WHERE user_name=%s',username)
        print(result)
        if result == 0:
            print("注册成功")
            cs1.execute('INSERT INTO userlist(user_name,password) VALUES(%s,%s)', (username,password))
            connec.commit()
        else:
            print("注册失败,用户名已存在")
        cs1.close()
    except Exception as e:
        print(e)
    finally:
        connec.close()


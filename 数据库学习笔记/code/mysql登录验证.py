from pymysql import *
from hashlib import sha1

if __name__ == '__main__':
    username = input('请输入用户名：')
    password = input('请输入密码')

    sh = sha1()
    sh.update(password.encode())
    password = sh.hexdigest()

    try:
        connnect_ = connect(host='localhost', port=3306,
                           database='test', user='root',
                           password='python', charset='utf8')
        cs1 = connnect_.cursor()
        result = cs1.execute('SELECT * FROM userlist WHERE user_name = %s',(username,))
        if result:
            # 用户名存在
            print('用户存在')
            # print(cs1.fetchone())
            result = cs1.fetchone()
            if result[2] == password:
                # 密码匹配成功
                print("登录成功")
            else:
                print('登录失败')
        else:
            print("用户名不存在")
    except Exception as e:
        print(e)
    finally:
        connnect_.close()
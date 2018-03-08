import pymysql
# 创建数据库对象


#先用pymysql生成表
connect = pymysql.Connect(
    user='root',
    passwd='python', #你的密码
    db='world',
    charset='utf8'
)
cursor = connect.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
connect.commit()    # 提交事务:
cursor.close()
connect.close()

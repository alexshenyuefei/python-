import mysql.connector


conn = mysql.connector.connect(user='root', password='python', database='world2')
# 创建游标
# 游标可以让用户提交数据库命令，并获得查询的结果行。
# 当游标创建好后，就可以执行查询或命令（或多个查询和命令），并从结果集中取回一行或多行结果。
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)  # 影响的行数
conn.commit()  # 提交事务
cursor.close()  # 关闭游标


#  新建查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭游标和连接
cursor.close()
conn.close()
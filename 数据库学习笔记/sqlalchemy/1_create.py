import sqlalchemy


from sqlalchemy import create_engine

"""
这里的echo设置为True可以使得后面我们可以在控制台看到操作涉及的SQL语言。如果你觉得麻烦，可以将其设置为False。
"""
# 数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
engine = create_engine('mysql+pymysql://root:python@localhost:3306/python',echo=True)
"""
create_engine返回的是一个Engine实例，它代表了指向数据库的一些非常核心的接口
。他会根据你选择的数据库配置而调用对应的DBAPI。
"""
"""
当第一次如Engine.execute()或者Engine.connect()的方法被调用时，Engine才会真正的建立起到数据库的DBAPI连接。
实际上，我们一般并不会直接使用Engine。
"""
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column,Integer,String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(10))
    fullname =Column(String(10))
    password = Column(String(10))

    def __repr__(self):
        return "<User(name='{1}', fullname='{2}', password='{3}')>" .format(self.name, self.fullname, self.password)

User.__table__

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
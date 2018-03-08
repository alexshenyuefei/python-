sqlalchemy中 
User.query.get
get是通过主键查询

表创建过之后,再次执行创建,哪怕原表增加了字段,也不会再次创建表

```python
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:python@localhost:3306/python',echo=True)
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
session = Session()
```


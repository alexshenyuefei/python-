# MySql之commit、rollback等事务控制命令

```mysql
create table test
(
 PROD_ID varchar(10) not null,
 PROD_DESC varchar(25)  null,
 COST decimal(6,2)  null
);
```

```mysql
#开始一次事务
start transaction;
insert into test
values('4456','mr right',46.97);
commit;     #位置1
```

```mysql
SELECT * FROM test;
start transaction;
insert into test
values('3345','mr wrong',54.90);
rollback;回滚到上次自动提交处
```

```mysql
#测试保存点savepoint
start transaction;
savepoint point1;
update test
set PROD_ID=1;
rollback to point1;  #回到保存点point1


release savepoint point1; #删除保存点

```


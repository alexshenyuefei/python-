

unique索引包含了unique约束，因为unique约束是通过unique索引实现的. 

为了实现唯一约束,数据库会强制定义一个唯一索引在数据库上面



### 方案一：使用ignore关键字

给不能重复的字段添加唯一索引约束unique

如果是用主键primary或者唯一索引unique区分了记录的唯一性,避免重复插入记录可以使用：

```sql
INSERT IGNORE INTO `table_name` (`email`, `phone`, `user_id`) VALUES ('test9@163.com', '99999', '9999');
```

有重复记录就会忽略,执行后返回数字0

缺点:'不能更新存在的字段',只是忽略插入的新字段.表只能保留第一次插入的数据.



### 方案二:使用Replace

REPLACE的运行与INSERT很相像,但是如果旧记录与新记录有相同的值，则在新记录被插入之前，旧记录被删除.

```
REPLACE INTO `table_name`(`col_name`, ...) VALUES (...);
```



REPLACE语句会返回一个数，来指示受影响的行的数目。该数是被删除和被插入的行数的和

如果是2,表明删了一行加了一行.

如果是1,表名加了一行.



### 方案三:ON DUPLICATE KEY UPDATE

当符合某种条件的数据存在时，去修改它，不存在时，则新增

在INSERT INTO…..后面加上 ON DUPLICATE KEY UP,

假设a字段有唯一约束

```
INSERT INTO table (a,b) VALUES (1,2)  
  ON DUPLICATE KEY UPDATE b=b+1;
```

例子

```
INSERT INTO book(title,author)VALUES('飞狐外传','10') ON DUPLICATE KEY UPDATE author='10';
```

如果插入了一个新行，则受影响的行数是1，如果修改了已存在的一行数据，则受影响的行数是2



优点:不会删除原来行,就地更新
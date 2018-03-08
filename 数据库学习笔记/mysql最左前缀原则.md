### 最左前缀

通过实例理解单列索引、多列索引以及最左前缀原则

实例：现在我们想查出满足以下条件的用户id： 

```mysql
mysql>SELECT ｀uid｀ FROM people WHERE lname｀=’Liu’ AND ｀fname｀=’Zhiqun’ AND ｀age｀=26 
```


因为我们不想扫描整表，故考虑用索引。



#### 创建单列索引：

ALTER TABLE people ADD INDEX lname (lname); 

上述查询语句,通过单列索引查到lname=’Liu’对应的结果集,然后再遍历结果集1查找fname｀=’Zhiqun’,最后在lname=’Liu’ and fname｀=’Zhiqun’结果集中再遍历查找｀age｀=26 



注：在mysql中执行查询时，只能使用一个索引，如果我们在lname,fname,age上分别建索引,执行查询时，也只能使用一个索引，mysql会选择一个最严格(获得结果集记录数最少)的索引。



#### 多列索引： 

ALTER TABLE people ADD INDEX lname_fname_age (lame,fname,age); 
为了提高搜索效率，我们需要考虑运用多列索引

在创建多列索引时，要根据业务需求，where子句中使用最频繁的一列放在最左边。

##### 同时也常对text和blob字段使用多列索引



### 多列索引的正确使用-最左前缀

如果使用多列索引，where条件中字段的顺序非常重要，需要满足最左前缀列。

多列字段做索引，state/city/zipCode，想要索引生效的话，只能使用如下的组合

state/city/zipCode
state/city
state
其他方式（如city，city/zipCode），则索引不会生效



SELECT * FROM table WHERE state = 1 AND city = 2 AND zipCode = 3;
或者
SELECT * FROM table WHERE state = 1 AND city = 2 AND zipCode < 3;
的state/city/zipCode都会走索引

ELECT * FROM table WHERE state = 1 AND city >2 AND zipCode < 3;

则不会走索引



多列索引是先按照第一列进行排序，然后在第一列排好序的基础上再对第二列排序，如果没有第一列的话，直接访问第二列，那第二列肯定是无序的，直接访问后面的列就用不到索引了。



### [MySQL](http://lib.csdn.net/base/mysql)多列索引适合的场景

1.全字段匹配

2.匹配部分最左前缀

3.匹配第一列

4.匹配第一列范围查询(可用用like a%,但不能使用like %b)

5.精确匹配某一列和和范围匹配另外一列



```
有一种例外可以不使用聚集索引就能查询出所需要的数据， 这种非主流的方法 称之为「覆盖索引」查询， 也就是平时所说的复合索引或者多字段索引查询。 文章上面的内容已经指出， 当为字段建立索引以后， 字段中的内容会被同步到索引之中， 如果为一个索引指定两个字段， 那么这个两个字段的内容都会被同步至索引之中。
先看下面这个SQL语句
//建立索引
create index index_birthday on user_info(birthday);
//查询生日在1991年11月1日出生用户的用户名
select user_name from user_info where birthday = '1991-11-1'
这句SQL语句的执行过程如下
首先，通过非聚集索引index_birthday查找birthday等于1991-11-1的所有记录的主键ID值
然后，通过得到的主键ID值执行聚集索引查找，找到主键ID值对就的真实数据（数据行）存储的位置
最后， 从得到的真实数据中取得user_name字段的值返回， 也就是取得最终的结果
我们把birthday字段上的索引改成双字段的覆盖索引
create index index_birthday_and_user_name on user_info(birthday, user_name);
这句SQL语句的执行过程就会变为
通过非聚集索引index_birthday_and_user_name查找birthday等于1991-11-1的叶节点的内容，然而， 叶节点中除了有user_name表主键ID的值以外， user_name字段的值也在里面， 因此不需要通过主键ID值的查找数据行的真实所在， 直接取得叶节点中user_name的值返回即可。 通过这种覆盖索引直接查找的方式， 可以省略不使用覆盖索引查找的后面两个步骤， 大大的提高了查询性能
```
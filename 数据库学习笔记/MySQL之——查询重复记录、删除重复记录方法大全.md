http://blog.csdn.net/l1028386804/article/details/51733585

### 一、查找重复记录

#### 1、查找全部重复记录

```mysql
Select * From 表 Where 重复字段 In (Select 重复字段 From 表 Group By 重复字段 Having Count(*)>1)  
```

#### 2、过滤重复记录(只显示一条)

```mysql
Select * From HZT Where ID In (Select Max(ID) From HZT Group By Title)  
```

### 二、删除重复记录

1、删除全部重复记录（慎用）

```
Delete 表 Where 重复字段 In (Select 重复字段 From 表 Group By 重复字段 Having Count(*)>1)  
```

### 2、保留一条（这个应该是大多数人所需要的 ^_^）

```
Delete HZT Where ID Not In (Select Max(ID) From HZT Group By Title)  
```



### 三、举例
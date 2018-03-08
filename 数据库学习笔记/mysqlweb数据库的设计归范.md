### mysql web数据库的设计归范-1命名规范



摘要: mysql 现在应用于web方向，游戏方向和OLAP方向。发现在平时运维中，很多开发错用，乱用mysql，什么功能都堆到数据库上，下面简单聊一聊web方向，mysql应该如何设计和使用。

**[数据库环境介绍]**

通常来讲，各个互联网公司的数据库分为5个数据库环境：

[数据库环境介绍]

通常来讲，各个互联网公司的数据库分为5个数据库环境：

1. dev : 开发环境, 开发可读写,可修改表结构; 常用的163的数据库表; 开发人员可以修改表结构, 可以随意修改其中的数据; 但是需要保证不影响其他开发同事; 

2. qa : 测试环境, 开发可读写, 开发人员可以通过工具修改表结构; 

3. sim: 模拟环境, 开发可读写, 通过web平台;发起上线请求时，会先在这个环境上进行预执行， 这个环境也可供部署上线演练或压力测试使用 可以读写;

4. real: 生产数据库从库（准实时同步）,只读环境,不允许修改数据,不允许修改表结构; 供线上问题查找,数据查询等使用;

5. online: 线上环境;开发人员不允许直接在线上环境进行数据库操作,如果需要操作必须找DBA进行操作并进行相应记录;

   ​这些环境的机器，一定要做到权限划分明确，读写帐号分离，并且有辨识度，能区分具体业务。例如用户名w_wap, r_wap 能看出来，读写帐号是wap应用的。	



[数据库命名规范]

\1. 尽量简洁明义，能够一眼看出来这个数据库是用来做什么的；

\2. 使用名词作为数据库名称，并且只用英文，不用中文拼音；

\3. 使用英文字母，全部小写，控制在3-7个字母以内；

\4. 如果有多个单词，则使用下划线隔开，不建议驼峰命名；

例如，每个公司都有crm业务，那就叫做xx_crm, 字符集统一utf8。字符集踩过的坑很多，为了通用性统一utf8。

```mysql
create database xx_crm default character set=utf8;
```



**[表命名规范]**

\1. 具备统一前缀，对相关功能的表应当使用相同前缀，如acl_xxx，house_xxx,ppc_xxx；其中前缀通常为这个表的模块或依赖主实体对象的名字，通常来讲表名为：业务 _ 动作 _  类型(不要空格)，或是业务_类型；

\2. 表名使用英文小写单词，如果有多个单词则使用下划线隔开；

3.表名简介，使用常见单词，避免使用长单词和生僻词；

\4. 表引擎取决于实际应用场景及当前数据库中的已经存在的存储引擎；日志及报表类表建议用myisam，与交易，审核，金额相关的表建议用innodb引擎。总体来讲数据库默认innodb；

\5. 数据表必须有主键，且建议均使用auto_increment的id作为主键（与业务无关）,和业务相关的要做为唯一索引；

\6. 默认使用utf8字符集（由于数据库定义使用了默认，数据表可以不再定义，但为保险起见，建议都写上）；

\7. 所有的表都必须有备注，写明白这个表中存放的数据内容；

\8. 预估表数据量，如果数据量较大（超过500w）则需要考虑分表策略。可以等量均衡分表或根据业务规则分表均可。要分表的数据表必须与DBA商量分表策略；

\9. 职责相近的表，命名规则应该相同；如合同申请，账户信息，交友相关等；

举个例子，一张在线冲值记录表：user_bank_deposit 这个就非常符合标准，如果叫做userBankDeposit或是user_chongzhi，就非常不友好。

user-用户业务

bank-将（钱）存入银行

deposit-储蓄

```mysql
CREATE TABLE `house_refresh_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `fangid` int(11) NOT NULL COMMENT '房贴子ID',
  `refresh_time` int(11) NOT NULL COMMENT '刷新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `fangid` (`fangid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='房刷新记录表'
```



[字段命名规范]

1. 数据库字段命名与表名命名类似：
2. 使用小写英文单词，如果有多个单词使用下划线隔开；
3. 使用简单单词，避免生僻词；
4. 字段应当有注释，描述该字段的用途及可能存储的内容，如枚举值则建议将该字段中使用的内容都定义出来；
5. 是别的表的外键均使用xxx_id的方式来表明；
6. 表的主键一般都约定成为id，自增类型；
7. 时间字段，除特殊情况一律采用int来记录unix_timestamp；
8. 网络IP字段，除特殊情况一律用bigint来记录inet_aton值；备注:IP转数字函数inet_aton(),数字转IP函数inet_ntoa(),用来将数字和ip地址互相转化.
9. 所有字段，均为非空，最好显示指定默认值；
10. 有些驱动对tinyint支持不够好，通常建义按容量来选择字段；
11. text字段尽量少用，或是拆到冗余表中；



```mysql
CREATE TABLE `wanted_post` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `puid` int(10) unsigned NOT NULL,
  `user_id` int(10) NOT NULL COMMENT '发贴用户的id',
  `username` varchar(50) NOT NULL COMMENT '发贴用户的用户名',
  `city` smallint(4) NOT NULL COMMENT '所在城市',
  `ip` bigint(14) NOT NULL COMMENT '发帖人的ip',
  `district_id` tinyint(2) NOT NULL COMMENT '所在区域的id',
  `district_name` varchar(20) NOT NULL COMMENT '行政区名字',
  `street_id` tinyint(2) NOT NULL COMMENT '所在街道(地标)的id',
  `street_name` varchar(20) NOT NULL COMMENT '小区名字',
  `title` varchar(255) NOT NULL COMMENT '帖子的标题',
  `description` text NOT NULL COMMENT '帖子详情描述',
  `post_at` int(11) NOT NULL COMMENT '用户发帖时间,数据创建的时间,使用整型存储',
  `refresh_at` int(11) NOT NULL COMMENT '帖子被修改的时间,整型存储',
  `show_time` int(11) NOT NULL COMMENT '帖子显示时间',
  `age_max` int(11) NOT NULL DEFAULT '0' COMMENT '招聘最小年龄',
  `age_min` int(11) NOT NULL DEFAULT '0' COMMENT '招聘最大年龄',
  `post_refresh_at` int(11) NOT NULL COMMENT '刷新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_puid` (`puid`),
  KEY `user_id_index` (`user_id`),
  KEY `post_at_index` (`post_at`),
  KEY `refresh_at_index` (`refresh_at`),
  KEY `show_time_index` (`show_time`)
) ENGINE=InnoDB AUTO_INCREMENT=55295 DEFAULT CHARSET=utf8 COMMENT='招聘帖子表'
```

mysql5字段定义时，是定义的【字符】数。比如varchar(10)，你仅能存入10个英文字母或者汉字，尽管一个字符可能占多个字节。

使用 UNIQUE 约束确保在非主键列中不输入重复的值。尽管 UNIQUE 约束和 PRIMARY KEY 约束都强制唯一性，但想要强制一列或多列组合（不是主键）的唯一性时

应使用 UNIQUE 约束而不是 PRIMARY KEY 约束。

add index 索引名称(数据库字段名称) 

AUTO_INCREMENT = 100;（ID列从100开始自增）






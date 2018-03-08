## mysql web数据库的设计归范-2表设计原则

**[职责分离原则]**

职责分离原则是指在设计的时候应当考虑到数据的产生，聚合使用等原则，每个系统干自己能干的事情，每个系统只干自己的事情。一个数据表应该放在哪个系统中，通常取决于几点：

\1. 谁产生这个信息：通常情况下谁产生了这个数据应当对此数据负责；也就是考虑该数据的创建，发展，销毁等全生命周期的定义，并将这个定义维护起来提供给消费者作为消费原则；

\2. 谁最经常使用这个信息：如果某个系统最经常使用这个数据，最经常去修改某个数据，也应该由该系统来负责保存维护该数据；

\3. 遵守高内聚，低耦合的考虑：在存放数据的时候如果考虑到数据使用原则导致了相关度非常高的数据存放在多个地方，需要多个系统来维护这个数据就有可能导致系统间的耦合性增强，应当尽量避免。

在我们设计数据库表间的关系的时候也应当遵守相同原则，职责分离降低耦合，但同时要考虑到性能情况，做到适当冗余而不导致修改逻辑复杂。

举个最常见贴子与评论的例子：

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


CREATE TABLE `wanted_post_comment_99` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `puid` int(10) unsigned NOT NULL,
  `user_id` int(10) NOT NULL COMMENT '评论用户ID',
  `post_at` int(11) NOT NULL COMMENT '评论时间',
  `detail` text NOT NULL COMMENT '评论详情',
  PRIMARY KEY (`id`),
  KEY `user_id_index` (`user_id`),
  KEY `puidid_index` (`puid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COMMENT='招聘评论分表99'
```

由于评论表数据量很大，在预先做好分表，按贴子puid分成100张子表，那么当前详情页涉及sql如下：

```sql
select * from wanted_post where puid=xxxx;
select * from wanted_post_comment_99 where puid=xxxx;
```

这是一个简化的模型，评论多了，还要涉及分页，不可能一次性全取出来。对于上面的场景，严格尊守高内聚，低耦合的原则，不会存储冗余数据。相比较还有一种文档型数据库，例如mongo，就可以将评论与贴子存放在一起，访问的时候只需一次顺序IO操作。整体来讲表设计，要按照职责划分原则。



**[在线处理与分析分离]**

\1. 为了保障线上数据处理的性能，将一些分析相关的数据及分析结果，应当使用单独的库来进行存储，避免在数据分析的时候导致业务数据吞吐量下降，引起系统问题。

\2. 专门用于存放离线报表数据，并提供线上数据查询方法，建议将统计结果，汇总的数据都从在线处理数据库中移走。

对于上面的wanted_post求职贴子表，在线处理只能是用户在操作：浏览，修改，删除，分别对应如下sql：

```sql
select * from wanted_post where puid=xxxxx;
update wanted_post set xxx=xxx where puid=xxxx;
delete from wanted_post where puid=xxxx;
```



同样，对于后台统计来讲，都是些聚合操作，非常消耗性能，例如查看某一用户发贴量：

```sql
select count(*) from wanted_post where user_id=xxxx;
```



上面举个通用的例子，原则上要将在线用户请求和后台统计请求分开。简单来讲，对于这种需求处理如下：

1. 将请求指向不同slave ，这种方法简单高效，缺点是数据量增大就玩不转。
2. 建立离线报表库，专门存放统计结果，这样将计算与展示异步处理，缺点是对于实时业务响应不好。
3. 实时拉取mysql row binlog，做数据的异构处理(tungsten, canal)，将增量结果处理后(storm)，保存在数据库中，基本实时。



**[事务与日志分离]**

用户生成内容和用户行为日志要分开，这一点很好理解，举两个例子：

1. 游戏DB里存放玩家的基础信息，装备，属性，好友列表等等，这些放到数据库里面。但是玩家的行为日志，比如消耗金币，今天下过哪些副本，买过什么顶级装备，这些属于行为日志，应该单独存放并分析处理。 
2. 对于web用记，有好多用户置顶，刷新，竞价，展示等行为，要求实时并且量很大，一定要和贴子分开。

行为日志，需要做分析处理，并且由于时效性不宜存储在mysql中，后期维护就是地雷。



**[历史可追溯]**

在数据库设计的时候为了保障数据是可追溯的，应当遵循一些简单的约定，事后方便数据的查询和统计：

\1. 对于状态数据，应当设计相应状态的字段来保存该数据的最后状态，同时记录下来该数据的初始创建人，时间以及该数据的最后修改人和修改时间；所以在交易数据（如订单合同），广告数据，账户表等都应该默认有状态（status），创建人（creator/creator_name），创建时间（created_at），最后修改人（modifier/modifier_name），最后修改时间（modified_at）等字段用来表明数据的当前状态，创建信息及修改信息。

\2. 针对需要跟踪每次修改的数据，需要在数据发生变化的时候记录一张日志表，用于记录该数据发生变化的全生命周期。针对只需要关注关键字段变化的情况，则日志表中只需要记录关键字段变化即可，但操作人，操作类型，时间应当准确记录，日志表数据一旦生成不允许进行修改。如用户账户的充值流水，消费流水都是一些业务紧相关的日志。而审核日志，操作记录等日志则属于与业务关联较小的日志。

\3. 针对所有历史需要保留的数据则需要每次变化都生成一个新的版本，比如类目信息等，对原始数据永远只做insert操作，不做delete及update操作。但这种情况仅限于极端数据历史要求极高的情况下使用。
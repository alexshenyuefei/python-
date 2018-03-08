Django 的 Model 驱动对数据库层面上的实现细节关注的非常少，开发者定义模型的过程非常接近声明式而非过程式，对于新项目来说，可能是这个原因让 Django Model 比 SQLAlchemy 讨人喜欢。

传统的 SQLAlchemy 的使用方法是不入侵模型，在单独的地方定义表结构、映射规则，然后用 SQLAlchemy 驱动注入到模型类里去，这种方法可以完全避免模型与数据库的耦合，但是定义繁琐，要求开发者完全明白 engine、metadata、table、column、mapper 等概念，如果没有读过《企业应用架构模式》一类书籍会被弄得很乱。

现在 SQLAlchemy 提供了 declarative 的方式，和 Django Model 很像，但是和声明式模型还是有一定的距离，好在对于灵活性几乎没损失。但是我对比了一下 Django Model 和 SQLAlchemy declarative，发现 Django Model 还是更简洁一些。例如对于类关联，Django 只要直接声明外键，就自动产生关联对象，而 SQLAlcyhemy 要定义外键、relationship 对象，如果有多个外键还要自己指定 join 规则…… 总之灵活性是好东西，但是不是什么情况下都讨人喜欢的。

我本来想说这个是 ActiveRecord style 和 Data Mapper style 区别导致的，但是细想了一下，Django Model 并不是简单的 ActiveRecord，其对于复杂关联甚至继承的映射都有很好的适应性，应该和 SQLAlchemy 的 declarative 是同类型的，是对 Data Mapper 的 Active Record style 包装。

作者：松鼠奥利奥

链接：https://www.zhihu.com/question/19959765/answer/1383267
db['artilces'].update({'title':data['title']},{'$set':data},True):

在articles表中.根据date[title]的值,找到title字段一样值所在行.将数据全部更新.

设置True,根据前面设置的data['title']参数查找title字段里面相同的,如果查找到执行更新,没查找到执行插入.
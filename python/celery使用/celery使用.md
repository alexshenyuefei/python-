生产上使用multy命令,这样断开ssh连接服务也不会关闭



执行一个异步任务,后端把没完成的celery任务id给前端



前端每间隔一段时间,使用ajax 将任务id询问后端接口,任务完成则返回结果.



异步执行耗时任务,避免了一个任务耗时很长时间,倒是导致函数一直没有返回数据,前端页面一直在转圈.



from celery.result import AsyncResult

通过celery任务id取到结果

result = AsyncResult(id='')

result.get() 

result.status(pending和success两种状态)

获得result的状态,和result的值(如果是success状态)






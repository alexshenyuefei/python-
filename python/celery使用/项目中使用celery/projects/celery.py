from __future__ import absolute_import, unicode_literals # 用于和python2兼容,python3可以不加这一行
from celery import Celery

app = Celery('projects', #这里和项目文件夹一致,这里项目文件夹叫projects,也可以自己取名字,Celery第一个参数是给其设定一个名字
             broker='redis://127.0.0.1:6379/3',
             backend='redis://127.0.0.1:6379/3',
             include=['projects.tasks'])# 指明任务文件所在位置

# Optional configuration, see the application user guide.
# 任务过期时间
app.conf.update(
    result_expires=3600,
)
"""
broker主管任务调度
backend存储返回数据
"""
if __name__ == '__main__':
    app.start()
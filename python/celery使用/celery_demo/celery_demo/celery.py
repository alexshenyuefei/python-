from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
# 让celery知道djano和django项目的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_demo.settings') #和项目名一致

app = Celery('celery_demo')# 和项目名一致

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# 可以把Celery的设置写入setting文件里,必须以CELERY_开头
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
"""
With the line above Celery will automatically discover tasks from all of your installed apps, following the tasks.py convention:
注册的django项目中所有名字为tasks.py文件会被Celery自动扫描
"""


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
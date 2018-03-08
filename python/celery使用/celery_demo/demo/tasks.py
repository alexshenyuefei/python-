# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

# 各个app都可以导入这个任务
@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def avalon(strings):
    print(strings,'avalon')
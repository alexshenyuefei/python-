from celery import Celery
from celery.schedules import crontab

app = Celery(broker='redis://127.0.0.1:6379/3',
             backend='redis://127.0.0.1:6379/3',)

CELERY_TIMEZONE = 'Asia/Shanghai' # 设置时区

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # 每10秒调用test('hello')函数
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    # 每30秒调用test('hello')函数
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # 在每周日的1:35调用test('Happy Mondays!')函数
    sender.add_periodic_task(
        crontab(hour=1, minute=35, day_of_week='sun'),# 具体参数看快速入门文档
        test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)


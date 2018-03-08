from celery import Celery
import time
app = Celery('tasks',
             broker='redis://127.0.0.1:6379/3',
             backend='redis://127.0.0.1:6379/3')


@app.task
def add(x, y):
    time.sleep(20)
    print("running...", x, y)
    return x + y

@app.task
def chufa(x,y):
    time.sleep(10)
    print('除法',x,y,'正在执行')
    return x/y
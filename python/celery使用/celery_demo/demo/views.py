from django.shortcuts import render, HttpResponse
from celery.result import AsyncResult
# Create your views here.
import base64
from demo import tasks



"""
这里是同步调用，不太好
以后项目中返回res即任务的id，通过id找结果更好
"""

def task_test(request):
    res = tasks.add.delay(228, 24)
    print("start running task")
    print("async task res", res.get())

    return HttpResponse('res %s' % res.get())


def task_res(request):
    """通过任务id号获得结果,前端通过ajax+base64加密发送,后端解密然后根据id号得到结果返回,实现异步."""
    result = AsyncResult(id="8759c00e-8d22-4e80-a65d-20d999bce200")

    #return HttpResponse(result.get())
    return HttpResponse(result.status)
#模拟base64编码解码
def b64():
    a = "8759c00e-8d22-4e80-a65d-20d999bce200"
    a = a.encode()
    a = base64.urlsafe_b64encode(a) #  b'ODc1OWMwMGUtOGQyMi00ZTgwLWE2NWQtMjBkOTk5YmNlMjAw'
    b = base64.urlsafe_b64decode(a)
    b.decode()
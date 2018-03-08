# Exception是所有异常的基类,except Exception 意味着捕获所有异常
try:
    print("foo")
except Exception as e:
    print(e)

# 自定义一个异常,并且捕获.
class MyError(Exception):
    def __init__(self,msg):
        self.msg = msg
        self.m = " 抛出Myerror异常"

    def __str__(self):
        return self.msg+self.m

def age(n):
    try:
        if n <0:
            raise MyError("年龄不能为0以下")
    except MyError as ex:
        print(ex)
    else:
        print("抛出异常时候不会执行else")
age(-9)
# age(99)
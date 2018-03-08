class D(object):
    pass

class A(D):
    @classmethod
    def as_view(cls):
        print("a")
        print(cls.__mro__)
        super(A,cls).as_view()

class B(object):
    @classmethod
    def as_view(cls):
        print("执行了B的as_view类方法")


class C(A,B):
    pass

C.as_view()
print(C.__mro__)
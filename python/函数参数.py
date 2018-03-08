def foo(a:str,b=10,c=100,*arg,**kwargs):
    print(a, b ,c ,arg ,kwargs)

foo('acc',2,100,9,10,'',g=1000,f=10000,h=999)
# hasattr(object, name)
def method_a(self):
    return 'hello'


ins = type('Fake', (), {'a': 1, 'b': 2,'method_a':method_a})()
print(hasattr(ins,"a"))
print(hasattr(ins,"c"))

# getattr(object, name[,default])
"""
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
需要注意的是，如果是返回的对象的方法,返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号。
"""
print(getattr(ins,"method_a",'avalon'))
print(getattr(ins,"method_a",'avalon')())
print(getattr(ins,"method_b",'avalon'))


# setattr(object, name, values)
# 给对象的属性赋值，若属性不存在，先创建再赋值。
getattr(ins, "age", setattr(ins, "age", "18")) #age属性不存在时，设置该属性
print(ins.age)
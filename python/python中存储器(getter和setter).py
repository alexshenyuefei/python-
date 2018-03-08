"""
属性的getter和setter
由getter和setter定义的属性叫做"存取器属性,不同于数据属性,数据属性只有一个简单的值.
程序查询存取器属性的值时,python调用getter方法(无参数),这个方法的返回值就是属性存取表达式的值.
程序设置一个存取器属性的值时,python调用setter方法,将赋值表达式右侧的值当做参数传入setter-这个方法负责"设置"属性值.
如果属性同时具有getter和setter方法,它是一个读/写属性.只有getter方法,它只是一个只读属性,只有setter方法,它是一个只写属性
"""
# 通过point属性设置点坐标,并返回距离
"""
42.将存取器属性的getter和setter方法看成属性的特性.可以把数据属性的值也看做属性的特性.
	一个属性包含一个名字和四个特性,它的值(value),可读写性(writeable),可枚举性(eunmerable)和可适配性(configurable)
    存取器不具备值特性,和可写性,它的可写性是由setter方法决定的
"""
class Point(object):
    def __init__(self):
        self.x = 1
        self.y = 1

    def get_distance(self):     #设置存储器类型属性的getter
        distance = (self.x**2 + self.y**2)**0.5
        return distance

    def set_point(self,value:tuple):    #设置存储器类型属性的setter
        self.x, self.y = value

    point = property(get_distance,set_point) #定义实例对象属性point,设置值时调用set_point,获取值时调用getdistance.

pointone = Point()
print(pointone.point)  #对象属性point,获取值时调用get_distance
pointone.point = (10, 10)  #对象属性point,设置坐标值,调用set_point
print(pointone.point)
# 通过point属性设置点坐标,并返回距离
class Point(object):
    def __init__(self):
        self.x = 1
        self.y = 1

    @property   #使用装饰器对point进行装饰，那么会自动添加一个叫point的属性，当调用获取point的值时，调用此下一行的方法
    def point(self):   #设置存储器类型属性的getter
        distance = (self.x**2 + self.y**2)**0.5
        return distance

    @point.setter   #使用装饰器对point进行装饰，当对point设置值时，调用下一行的方法
    def point(self,value:tuple):    #设置存储器类型属性的setter
        self.x,self.y = value


pointone = Point()
print(pointone.point)  #对象属性point,获取值时调用get_distance
pointone.point = (10, 10)   #对象属性point,设置坐标值
print(pointone.point)

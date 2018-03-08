# 模块和文件
"""
模块是按照逻辑来组织 Python 代码的方法, 那么文件便是物理层上组织模块的方法。
一个文件被看作是一个独立模块, 一个模块也可以被看作是一个文件。
模块的文件名就是模块的名字加上扩展名.
"""
"""
模块的导入需要一个叫做"路径搜索",在定义的搜索路径里,进行路径搜索.
在文件系统"预定义区域"中查找 mymodule.py文件(如果你import mymodule的话)
默认搜索路径是在编译或是安装时指定的。 它可以在一个或两个地方修改。
一个是启动 Python 的 shell 或命令行的 PYTHONPATH 环境变量
解释器启动之后, 也可以访问这个搜索路径, 它会被保存在 sys 模块的 sys.path 变量里。
import sys
sys.path
修改方法
sys.path.append('/home/wesc/py/lib')
sys.path.insert(1,'/home/wesc/py/lib')
"""
"""
使用 import 语句导入模块
导入顺序按照:
􀁺 Python 标准库模块
􀁺 Python 第三方模块
􀁺 应用程序自定义模块
"""
"""
重新导入模块
from imp import *
import mymodel
reload(mymodel)
"""
"""
包是一个有层次的文件目录结构, 它定义了一个由模块和子包组成的 Python 应用程序执行
环境。
要导入的目录里有.py文件就要有__init__.py
__init__.py 文件。 这些是初始化模块,
from-import 语句导入子包时需要用到它。
在__init__.py 中加入 __all__ 变量. 该变量包含执行from package.module import *时应该导入的模块的名字
相对导入
import 语句总是绝对导入的, 所以相对导入只应用于 from-import 语句。
from .Analog import dial 在当前目录导入Analog模块,导入Analog中的dial对象
from ..common_util import setup 在当前目录的前一个目录导入
阻止对象导入
想让某个模块属性被 "from module import *" 导入 , 那么你可以给你不想导入的属性名称加上一个下划线( _ )
但是如果指明,_还是不管用的.如import foo._bar
"""
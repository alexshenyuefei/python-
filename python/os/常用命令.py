import os
print(os.getcwd())  # 获取当前路径
print(os.path.abspath(__file__)) #获取当前文件绝对路径
print(os.path.abspath('.'))
print(os.path.basename(__file__)) # 返回文件名
print(os.path.dirname(__file__))# 返回文件路径
"""
os.listdir() # 列出当前目录下的所有文件和文件夹。
os.path.isfile()  # 判断指定对象是否为文件。是返回True,否则False
os.path.isdir()  # 判断指定对象是否为目录。是True,否则False。
os.path.exists()  # 检验指定的对象是否存在。是True, 否则False.
"""
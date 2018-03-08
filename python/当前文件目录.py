import os
now_file_path=os.path.abspath(__file__) #当前文件绝对路径
print(now_file_path)

now_file_path_dir = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在目录
print(now_file_path_dir)

temps = os.path.join(now_file_path_dir,'temp') # 当前目录下temp目录
print(temps)
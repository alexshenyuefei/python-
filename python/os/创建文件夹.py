import os
now_dir_path = os.path.dirname(os.path.abspath(__file__))
print(now_dir_path)
# os.mkdir('d:\hello')
os.mkdir(now_dir_path+'\\创建文件夹')
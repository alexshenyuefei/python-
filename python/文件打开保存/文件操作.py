# file_object = open(file_name, access_mode='r', buffering=-1)
'''
file_name 是包含要打开的文件名字的字符串, 它可以是相对路径或者绝对路径. 可选变量
access_mode 也是一个字符串, 代表文件打开的模式. 通常, 文件使用模式 'r', 'w', 或是 'a'
模式来打开, 分别代表读取, 写入和追加. 还有个 'U' 模式, 代表通用换行符支持
使用 'r' 或 'U' 模式打开的文件必须是已经存在的. 使用 'w' 模式打开的文件若存在则首
先清空, 然后(重新)创建. 以 'a' 模式打开的文件是为追加数据作准备的, 所有写入的数据都将
追加到文件的末尾.
'b'代表bytes模式访问.
如果你要处理一个二进制文件, 并希望你的程序可以移植到其它非Unix 的环境中, 加上"b" 会是不错的主意
r+为可读写两种操作    w+为可读写两种操作（会首先自动清空文件内容）
'''
# fp = open('abc.txt', 'w') # 以写方式打开
# fp = open('abc.txt', 'r') # 以写方式打开
fp = open('abc.txt', 'r+',encoding='utf-8') # 以读写方式打开,字符编码是utf-8
# fp = open(r'abc.txt', 'rb') # 以二进制读模式打开,输出类型是bytes类型
print(fp.readlines())  # readline() 方法读取打开文件的一行,readlines() 方法并不像其它两个输入方法一样返回一个字符串. 它会读取所有(剩余的)行然后把它们作为一个字符串列表返回
fp.write('avalon')  # 它把含有文本数据或二进制数据块的字符串写入到文件中去,没有 "writeline()" 方法, 因为它等价于使用以行结束符结尾的单行字符串调用write() 方法.

fp.read() #返回所有读取数据
"""
file.encodinga 文件所使用的编码 - 当 Unicode 字符串被写入数据时, 它们将自动使
用 file.encoding 转换为字节字符串; 若file.encoding 为 None 时使
用系统默认编码
"""
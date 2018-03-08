# with open('阿瓦隆1.txt','w') as f:
#     f.write('遗世独立的理想乡')
#     f.write('\r\n')
#     f.write('亚瑟王')
# with open('阿瓦隆1.txt','rU') as f:
#     print(f.read().__repr__())
"""
python3d读取不推荐rU模式
"""
# f = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)
"""
在Python 3，可以通过open函数的newline参数来控制Universal new line mode：读取时候，不指定newline，
则默认开启Universal new line mode，所有\n, \r, or \r\n被默认转换为\n ；
写入时，不指定newline，则写入'\n'为各系统默认的换行符（\n, \r, or \r\n, ），指定为newline='\n'，则都替换为\n（相当于Universal new line mode）；
不论读或者写时，newline=''都表示不转换。
"""
"""
On input, if newline is None, universal newlines mode is enabled. Lines in the input can end in '\n', '\r', or '\r\n', and these are translated into '\n' before being returned to the caller. If it is '', universal newline mode is enabled, but line endings are returned to the caller untranslated. If it has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.

On output, if newline is None, any '\n' characters written are translated to the system default line separator,os.linesep. If newline is '', no translation takes place. If newline is any of the other legal values, any '\n' characters written are translated to the given string.
"""
# with open('阿瓦隆.txt','w') as f:
#     f.write('亚瑟王')
#     f.write('\n')
#     f.write('\n')
#     f.write('\n')
#     f.write('阿尔托利亚')


with open('阿瓦隆.txt','r') as f:
    print(dir(f))
    print(f.read())
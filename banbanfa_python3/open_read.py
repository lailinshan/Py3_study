import os
from sys import argv
#定义携带参数
script,filename = argv
#打开文件(写入的内容追加在末尾)
o = open(filename,'a')
#写入内容到文件
o.write('adsf\n')
#关闭打开的文件
o.close()
#打开文件
o = open(filename,'r')
#读取文件
r = o.read()
#打印读取到的内容
print(r)
#关闭打开的文件
o.close()
#导入解包功能，运行脚本的时候需要传入对应参数的个数
from sys import argv
#定义argv 参数的个数
a,b,c,d = argv
s = 6
f = '>'
print(a)
print(b,c,d)
print(input('''"你输入了几个数字:"'''))
print(input(f))
print('%s' % b)
# print(type(b))
#condig:utf-8
# a = 1
# a1 = 1.3
# a2 = 'aaa'
# a3 = 1.3j
# print(type(a))#type 查看类型
# print(type(a1))
# print(type(a2))
# print(type(a3))
'''---------1th--------------------'''
# a = 9.8
# print(str(a))#str/int 可以强转类型
# a13 = 'sdfsdfds'
# print(repr(a13))#带''号输出字符串
# a11 = r"c:\a.txt'" #r输出原始字符，进行转义
# print(a11)
# a1 = bytes('我是谁！',encoding='utf-8')#转字节串
# b = '我是谁！'.encode('utf-8')
# print(a1)
# print(b)
# a12 = b.decode('utf-8')#解码
# print(a12)
'''-----------2th------------------'''
# b1 = 'one adsdfWWfds is ok good study'
# print(b1.title())#首字母大写
# print(b1.lower())#全部小写
# print(b1.upper())#全部大写
# print(b1.strip())#删除两端空格
# print(b1.lstrip())#删除左边空格
# print(b1.rstrip())#删除右边空格
# if b1.startswith('one') is True:#判断是否以XX开头
#     print('1')
# elif b1.endswith('study') is True:#判断是否以XX结尾
#     print('2')
# else:
#     print(b1.find('is'))#查找所在位置
#     print(b1.replace('s','S'))#替换字符，后面接数值可控制替换的个数，不加默认全部替换
# b2 = 'asd' if 1<2 else 'dsa' if 5 > 3 else 'weq'#三目运算
# print(b2)
# print(b1.split())#分割字符
# print(b1.split(None,2))
# print('/'.join(b1.split()))#以X连接字符串
# b3 = 66
# b4 = 'wa'
# b5 = ','.join(b4)
# print(bin(b3))
# print(oct(b3))
# print(hex(b3))
# b6 = hex(ord(b5[2]))#ord ASCII转码，字母转数字
# b7 = int(b6,16)
# print(chr(b7))#int(x,16)16进制转10进制，chr 数字转字母

# a = ('w',11,'e','r',22,'t','y')
# b = ['y','n',33,'u',66,'i','o','p','m']
# c = ['y','n','u','i','o']
# d = (1,3,8,9,10,5)
# print(a[::3])#切片间隔步长输出
# print(b[1:4])#切片指定输出步长范围内值
# #同类型可以相加，不同类型相加会报错
# print(a+a)
# print(a*3)
# print(b+b)
# print(b*3)
# try:
#     print(a+b)
# except:
#     print('元组和列表不能直接相加')
# print(len(b))#计算步长
# print(max(c))#计算最大值
# print(min(d))#计算最小值
'''-------------------------------'''
# a1 = 22,33,55 #封包
# print(a1)
# a2,a3,a4 = a1 #解包
# print(a2,a3,a4)
# b1,*b2,b3 = range(10)# '*'允许变量为列表，可以有多个值
# print(b1)
# print(b2)
# print(b3)
# b4 = tuple(range(10))#tuple将列表，区间等值转换成元组
# print(b4)
# print(tuple(b))
# c1 = [11,22,343]
# c1.append((111,155))#往后面追加元组
# c1.extend([116,787])#追加列表中的元素
# c1.insert(2,555)#指定位置追加
# del c1[2]#删除元素
# c1.remove(11)#移除第一个找个XX的元素
# # c1.clear()#清空元素
# c1[2]=22 #修改元素的值
# print(c1)
# print(c1.index(22))#查找XX在列表中的位置
# c2 = [33,1,4,5,66,66,88,6,55]
# c3 = ['aaaa','sss','dddddw','tert','aw']
# print(c2.count(66))#统计出现的次数
# c2.sort(reverse=True)#对列表进行排序,默认为从小到大，设置reverse为true实现从大到小排序
# c3.sort(key=len,reverse=True)#对比长度后 按长度大排序
# print(c2,c3)
# c2.reverse()#反转列表输出
# print(c2)

'''-------------------------------'''
d1 = dict(aa=1,ac=2,vf=6)#创建字典
print(d1)
#获取字典中key的值
print(d1['aa'])
print(d1.get('vf'))
del d1['ac']#删除字典中key和对应的值
d1['gf'] = 999#给字典追加key和值//列表list不允许对不存在的索引复制
print(d1)
#修改字典中key的值
d1['aa'] = 55
d1.update({'vy':99,'ap':'dd'})#可以实现更新或者追加
print(d1)
#判断XXkey是否在字典里面
print('vf' in d1)
print('vf' not in d1)
d5 = dict(aa=1,ac=2,vf=6)
d2 = d5.items()#字典转换成列表
d3 = d5.keys()#字典中key转成列表
d4 = d5.values()#字典中values转成列表
print(list(d2))
print(list(d3))
print(list(d4))
#格式化（没明白）
d6 = 'a:%(name)s,b:%(name2)s'
d7 = {'name':'aa','name2':'a33'}
print(d6 % d7)













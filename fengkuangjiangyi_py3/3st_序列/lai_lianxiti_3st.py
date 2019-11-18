#conding=utf-8
#导入随机数模块(生成随机数需要使用到)
import random
'''
1.提示用户输入N个字符串 ，将它们封装成元组，然后计算并输入该元组乘以3的结果，
再计算并输出该元组加上（ tkjava ’，’ crazy it ＇）的结果
'''
def list_change ():#优化前代码
    #使用try-except以防输入的不是数字，int转换格式时报错
    try:
        #input 默认为str类型，需要强转
        auserinputumber1 = int(input('<<请输入你想输入字符串的个数>>>\n'))
        print('<<请输入字符串>>>\n')
        alist1 = []
        atuple1 = ('tkjava','crazy it')
        #循环输入，并且把每次输入的值加到alist1中
        for a in range (auserinputumber1):
            alist1.append(input())
        alist2 = tuple(alist1)*3
        print(alist2)
        #list转元组
        alist3 = tuple(alist2)+atuple1
        print(alist3)
    except:
        print('<<输入的不是数字>>')
def list_change2 ():#优化后代码
    a1list = list(input('<<请输入字符串>>>\n'))
    atuple1 = ('tkjava', 'crazy it')
    print(tuple(a1list)*3)
    print((tuple(a1list)*3)+atuple1)
'''
2. 给定一个list ，将该列表的从 start到end的所有元素复制到另一个list
'''
def copy1 ():
    blist1 = ['ww','ds',666,'sdsd']
    #拷贝list
    blist2 =blist1.copy()
    print(blist2)

'''
3. 用户输入一个整数N，生成长度为N的列表，将N个随机数放入列表中
'''
def suijishu ():
    clist1 = []
    try:
        cuserinputumber1 = int(input('<<请输入一个正整数>>>\n'))
        while len(clist1) < cuserinputumber1:
            clist2 = random.randint(1,cuserinputumber1+255)
            if clist2 not in clist1:
                clist1.append(clist2)
        print(clist1)
    except:
        print('<<输入的不是正整数>>')

'''
4. 用户输入一个整数N，生成长度为N的列表，将N个随机的奇数放入列表中
'''
def qishu ():#只随机生成奇数
    dlist1 = []
    try:
        duserinputumber1 = int(input('<<请输入一个整数>>>\n'))
        while len(dlist1) < duserinputumber1:
            dlist2 = random.randint(1,duserinputumber1+255)
            if dlist2 % 2 != 0:
                dlist1.append(dlist2)
        print(dlist1)
    except:
        print('<<输入的不是数字>>')

def qishu2 ():#赛选随机数中的奇数
    dlist1 = []
    try:
        duserinputumber1 = int(input('<<请输入一个整数>>>\n'))
        dlist2 = list((random.randint(1, duserinputumber1 + 255)) for i in range(duserinputumber1))
        print('生成的原始列表是:',dlist2)
        for d3 in dlist2 :
            if d3 % 2 != 0:
                dlist1.append(d3)
        print('其中奇数是',dlist1)
    except:
        print('<<输入的不是数字>>')

'''
5. 用户输入一个整数N，生成长度为N的列表，将N个随机的大写字符放入列表中
'''
def euserinput ():
    elist1 = []
    try:
        euserinputumber1 = int(input('<<请输入一个整数>>>\n'))
        while len(elist1) < euserinputumber1:
            elist2 = chr(random.randint(ord('A'),ord('Z')+1))#字母转数字
            if elist2 not in elist1:
                elist1.append(elist2.upper())#转大写
        print(elist1)
    except:
        print('<<输入的不是数字>>')
'''
6. 用户输入N个字符串，将这些字符串收集到列表中，然后去除其中重复的宇符串后
'''
def remove ():#优化前代码
    try:
        #input 默认为str类型，需要强转
        fuserinputumber1 = int(input('<<请输入你想输入字符串的个数>>>\n'))
        print('<<请输入字符串>>>\n')
        flist1 = []
        #循环输入，并且把每次输入的值加到alist1中
        for f1 in range (fuserinputumber1):
            flist1.append(input())
        for f2 in range(fuserinputumber1 - 1):
            try:
                f3 = flist1.count(flist1[f2])
                if f3 > 1:
                    flist1.remove(flist1[f2])
            except:
                pass
        print(flist1)
    except:
        print('<<输入的不是数字>>')
def remove2 ():#优化后代码
    f3list = []
    for f2l in list(input('<<请输入你想输入字符串>>>\n')):
        if f2l not in f3list:
            f3list.append(f2l)
        print(f3list)
'''
7. 用户输入以空格分隔的多个整数，程序将这些整数转换成元组元素，并输出该元组（使用内置的 hash 函数）。
'''
def hash1 ():
    g = input('<<输入N个数，以空格间隔开>>\n')
    #列表转元组
    glist1 = tuple(g.split())
    #获取list的hash值
    glist2 = hash(str(g.split()))
    #获取元组的hash值
    glist3 = hash(str(glist2))
    print(glist1)
    print(glist3)
'''
8.用户随机输入N个大写字母，程序使用dict统计用户输入的每个字母的次数
'''
def dashen ():#大神的代码
    str1 = input("请输入大写字母")
    lstr = list(str1)
    a_dict = dict.fromkeys([chr(i) for i in range(ord('A'),ord('Z')+1)],0)
    for i in lstr:
        a_dict[i]+=1
    print(a_dict)

def study3 ():#学习第三章后写的
    #定义一个变量存放输入的值
    h1 = input("<<请输入字符>>\n")
    #列表化输入的字符串，这个变量循环后元素会后变化
    hlist1 = list(h1)
    #列表化输入的字符串，这个变量不参与循环，值保持初始状态
    hlist2 = list(h1)
    #获取列表长度用于控制第一个for循环
    h2 = int(len(hlist1))
    print('<<总共输入了{}个字符>>'.format(h2))
    #第一个for循环实现列表的去重
    for h3 in range(h2):
        try:
            if hlist1.count(hlist1[h3]) > 1:
                hlist1.remove(hlist1[h3])
        except:pass
    #以去重后的列表元素为key生成一个初始值为0的字典
    hdict1 = dict.fromkeys((tuple(hlist1)),0)
    for h4 in hlist2:#遍历列表实现统计
        hdict1[h4] += 1
    print(hdict1)

def study4 ():#参考第四章内容，更简洁的方法
    h1 = list(input("<<请输入字符>>\n"))
    dict1 = {}
    for h2 in h1:#遍历列表
        if h2 in dict1:#判断是key否已经在字典中，实现统计
            dict1[h2] += 1
        else:#设置key在字典中的初始值
            dict1[h2] = 1
    print(dict1)



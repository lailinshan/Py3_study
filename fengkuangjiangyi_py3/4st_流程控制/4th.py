#conding=utf-8
def fibonacci(X):
    if X == 0:
        return X
    elif X == 1:
        return X
    else:
        return  fibonacci(X-1)+fibonacci(X-2)

def main():
    index = int(input("<<>>\n"))
    print("fibonacci(",index,")=",fibonacci(index))
#if-elif-else
def ifelif1 ():
    age1 = int(input('<<请输入你的年龄>>\n'))
    if age1 >120:
        print('{}岁是有福气的长寿老者!'.format(age1))
    elif 60 < age1 <=120:
        print('{}岁是老年人了!'.format(age1))
    elif 40 < age1 <= 60:
        print('{}岁是中年大叔!'.format(age1))
    elif 20 < age1 <= 40:
        print('{}岁是个年轻小伙!'.format(age1))
    else:
        print('{}岁是个小孩子!'.format(age1))
#while循环
def while1 ():#while if 结合判断
    walist = [22,33,543,35,564,345,39,89,45,678]
    walist1 = []
    walist2 = []
    walist3 = []
    while len(walist) > 0 :
        sqe1 = walist.pop()
        if sqe1 % 3 == 0 :
            walist1.append(sqe1)
        elif sqe1 % 3 == 1 :
            walist2.append(sqe1)
        else:
            walist3.append(sqe1)
    print(walist,walist1,walist2,walist3)

def times1 ():
    numb1 = int(input())
    result1 = 1
    for numb12 in range (1,numb1+1):
        result1 *= numb12
        print('{}次循环:'.format(numb12),'result1等于:',result1)
#列表遍历
def forlist ():
    list2 = []
    list3 = []
    for i1 in range(1,6):
        list1 = input('<<请输入5个内容>>')
        try:
            if isinstance(int(list1),int):#判断类型
                list2.append(int(list1))
        except:
            list2.append(list1)
    for i in list2:
        if isinstance(i,int):
            a = i+1
            list3.append(a)
    print(list3)
#字典遍历
def fordict ():
    dict1 = {'aa':'3sd','we':1,'wer':'1g','11':66,'hj':'112','88':99,'lk':'ss','sse':36}
    for key , value in dict1.items():#items获取到的是两个元素的元组的列表，所以需要用两个变量
        print('key:',key)
        print('value:', value)
    print('第一个循环结束')
    for key in dict1.keys():
        print(key)
    print('第二个循环结束')
    for value in dict1.values():
        print(value)
    print('第三个循环结束')
#for 表达式
def listfor ():
    list2 = list(chr(x) for x in range(ord('a'),ord('z')+1))
    list3 = list(x1 for x1 in range(int(input())))
    print(list2)
    print(list3)
#数字转人民币读法
def money_to ():
    num = float(input())
    def divide(num):
        integer = int(num)
        fraction = round((num - integer)*100)
        return  (str(integer)),str(fraction)
    han_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
    unit_list = ['十','百','千']
    def four_to_hanstr(num_str):
        result = ''
        num_len = len(num_str)
        for i in range(num_len):
            num = int(num_str[i])
            if i != num_len - 1 and num != 0 :
                result += han_list[num] + unit_list[num_len - 2 -i]
            else:
                result += han_list[num]
        return  result
    def fraction_to_str (num_str2):#原代码基础上增加角分，以及单位‘圆’
        if int(num_str2) != 0:
            srt_len2 = len(num_str2)
            for i2 in range(srt_len2):
                if srt_len2 <= 1 :
                    return '圆'+four_to_hanstr(num_str2[i2-1]) + '角'
                else:
                    return '圆'+four_to_hanstr(num_str2[i2-1]) + '角' + four_to_hanstr(num_str2[i2]) + '分'
        else:
            return '圆'
    def integer_to_str(num_str):
        str_len = len(num_str)
        if str_len > 12 :
            print('数值太大无法翻译')
            return
        elif str_len > 8 :
            return  four_to_hanstr(num_str[:-8]) + '亿' + \
                four_to_hanstr(num_str[-8:-4]) + '万' + \
                four_to_hanstr(num_str[-4:])
        elif str_len > 4 :
            return four_to_hanstr(num_str[:-4]) + '万' + \
            four_to_hanstr(num_str[-4:])
        else:
            return  four_to_hanstr(num_str)
    integer, fraction = divide(num)
    integer_str = integer_to_str(integer)
    fraction_str = fraction_to_str(fraction)
    #（此方法性能差）以下判断方法参考：https://blog.csdn.net/qq_36652379/article/details/101726857
    if int(integer) > 0:
        integer_str = integer_str.replace("亿零", "亿")
        integer_str = integer_str.replace("万零", "万")
        integer_str = integer_str.replace("千零", "千")
        integer_str = integer_str.replace("百零", "百")
        integer_str = integer_str.replace("十零", "十")
        integer_str = integer_str.replace("零圆", "圆")
    print(integer_str + fraction_str)
#99乘法表
def A99():
    def A1():
        for i in range(1,10):
            for j in range(1,i + 1):
                print('%dX%d=%2d'%(j,i,i*j),end=' ')
            print('')
    def A2():
        for i in range(1,10):
            for j in range(i,10):
                print('%dX%d=%2d'%(i,j,i*j),end=' ')
            print('')
    def A3():
        for i in range(1, 10):
            for k in range(1, i):
                print(end="       ")
            for j in range(i, 10):
                print('%dX%d=%2d' % (i, j, i * j), end=' ')
            print('')
    def A4():
        for i in range(1, 10):
            for k in range(1, 10 - i):
                print(end="       ")
            for j in range(1, i + 1):
                print('%dX%d=%2d' % (j, i, i * j), end=' ')
            print('')
    A1(),A2(),A3(),A4()
#菱形
def linxing():
    # python3 一定要加，end=” “，好恶心
    n = int(input('请输入行数'))
    i=j=k=1
    for i in range(n):
        for j in range(n - i):
            print(" ", end=" ")  # 输出语句附加的字符串
            j = j + 1
        for k in range(2 * i - 1):  # 这里i最多等于3，打印前3行
            print("*", end=" ")
            k = k + 1
        print("\n")
        i = i + 1
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
            j = j + 1
        for k in range(2 * (n - i) - 1):  # i=4,从第四行开始打印
            print("*", end=" ")
            k = k + 1
        print("\n")
        i = i + 1
#三角形
def sanjiaoxing():
    a = int(input())
    def dengbian():
        for i in range(1, a):
            for j in range(1, a - i):
                print(" ", end="")
            print("* " * i)

    def Rzhijiao():
        for i in range(1, a):
            print("* " * i)
            for j in range(1, a):
                print(end="")

    def Lzhijiao():
        for i in range(1, a):
            for j in range(1, a - i):
                print(' ', end=" ")
            print("* " * i)
    dengbian()
    Rzhijiao()
    Lzhijiao()


'''
1.使用数值类型声明多个变量，并使用不同方式为不同的数值类型的变量赋值。熟悉每种数据类型的赋值规则和表达方式
2.使用数学运算符/逻辑运算符编写40个表达式，先自行计算各表达式的值，然后通过程序输出这些表达式的值进行对比，看看能否做到一切尽在掌握中
3.从标准输入读取两个整数并打印两行，其中第一行输出两个整数的整除结果；第二行输出两个整数的带小数的除法结果
4.从标准输入读取两个整数并打印三行，其中第一行包含两个数的和；第二行包含两个数的差；第三行包含两个数的乘积结果
5.输入一个字符串一个子串，程序必须打印出给定字串在目标字符串中出现的次数
6.用户输入一个字符串，修改该字符串中哪个位置的字符，程序就会输出修改后的结果。比如用户输入：‘fkjava.org’6 -  程序将输出：‘fkjava-org’
7;数值类型转化。  %nd,%ni,%no,%nx , %ns（转换为字符串）
'''
#conding=utf-8
'''
Part 1
2019.11.9
'''
#定义多个数值类型的变量
a = 1
b = 2
c = 3
d = 4
e = 5
#为变量赋值
#Tips：python为弱类型的语言，无需声明变量的类型。变量的类型与值的类型一致。
a = 10086 #int
b = 2.3456 #float
c = 'abc' #str
d = True #bool
e = [1,2,3] # list
f = (1,2,3) # tuple


'''
Part 2
2019.11.9
+ - * / & | ^ ~ <<  >>  > < >= <= == != is is not and or not 三目运算符  表达式 if 条件  else 表达式/输出  in
'''


#list=['+','-','*','//','>','<','>=','<=','!=','is','is not','in']
#tuple=(+,-,*,/,&,|,^,~,<<,>>,>,<,>=,<=,!=,is,is not,in)
'''
Tips:TypeError: 'list' object cannot be interpreted as an integer  列表类型对象不能直接作为range函数的参数传入
list=[a,b,c,d]
for i in range(list)会报错
'''
'''
1.定义运算符列表
2.定义运算表达式
3.定义随机参数
4.使用eval函数输出结果
'''
import random
#while True:
#list=['+','-','*','/','>','<','>=','<=','!=','is','is not','in']
list=['+','-','*','/']
x = random.choice(list)
#print(x)
if x == '+':
    a = random.randint(0,1000)
    b = random.randint(200,300)
    c =eval('%d %s %d '%(a,x,b))
    #c.append(a+b)
    #print(c)
if x == '-':
    a = random.randint(0,1000)
    b = random.randint(200,300)
    c =eval('%d %s %d '%(a,x,b))
    #c.append(a-b)
    #print(c)
if x == '*':
    a = random.randint(0,1000)
    b = random.randint(200,300)
    c =eval('%d %s %d '%(a,x,b))
    #c.append(a*b)
    #print(c)
if x == '/':
    a = random.randint(0,1000)
    b = random.randint(200,300)
    c =eval('%d %s %d '%(a,x,b))
    #c.append(a/b)
    #print(c)

'''
Part3 and 4
2019.11.9
'''
a=1 #int(input)
b=2
c=a/b
d=a//b
#print(c,d)

'''
Part 5
question:如何反向遍历
'''

a ='ab' #input()
b ='acbabbacbaba' #input()
print(len(a))
print(len(b))
# print(b[::len(a)])
# print(b[::3])
count = 0
# for i in range(len(b)):
#     if a == b[i:(i+len(a))]:
#         count +=1
#     #print(b[i:(i+len(a))])
# print(count)

'''
Part 6
输入字符串，使用空格分割
判断索引是否超出，未超出替换，超出返回错误
'''


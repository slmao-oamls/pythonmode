
# print('请输入名字：')
# name=input('请输入你的名字')
# print('hello,',name)

# a=10
# if a>=11:
# 	print(a)
# else:
# 	print(-a)

# print('''l1,\n
# l2
# l3''')

# age=16
# if age>=18:
#     print('adult')
# else:
#     print('teenager')

# n=123
# print(n)
# f=456.789
# print(f) s1='hello,world'
# s2='hello,\'adam\''
# s3=r'hello,"bart"'
# s4=r'''hello,
# slmao!'''
# print(s1,s2,s3,s4)

# a='123'
# b=a
# a='456'
# print(a,b)

# print('中文测试')

# print('hello,%s' % 'world')
# print('hi,%s,you have $%d.' % ('slmao',1000)) 
# print('%3d-%04d'%(3,1))
# print('%.2f'%3.1415926)


# print('age:%s.gender:%s'%(25,True))
# print('slmao rate:%d %%'%7)

# s1=72
# s2=85
# print('小明，成绩提升%.1f%%'% ((s2-s1)/s1*100))

# classmates=['michael','bob','tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0],classmates[-1])
# classmates.append('adam')
# print(classmates)
# classmates.insert(1,'jack')
# print(classmates)

# classmates.pop()
# print(classmates)
# classmates.pop(2)
# print(classmates)

# classmates[1]='slmao'
# print(classmates)

# l=['python','java',['asp','php'],136]
# print(l)
# print(len(l))
# print(l[2][0])

# tuples=('michael','bob','tracy')
# print(tuples)
# t=(1)
# print(t)
# t=(1,)
# print(t)

# t=('a','b',[1,2])
# t[2][0]='A'
# t[2][1]=3
# print(t)

# l=[['1','2','3'],(4,5,6),['adam',123,7.9]]
# print(l[0][0],l[1][2],l[2][2])

# age=3
# if age>=18:
# 	print('adult')
# elif age>=6:
# 	print('teenager')
# else:
# 	print('kid')

# x=1
# if x:
# 	print("True")

# b=int(input("birth:"))
# if b<2000:
# 	print("00前")
# else:
# 	print("00后")

# weight=80.5
# height=1.75
# bmi=weight/height
# if bmi>32:
# 	print('严重肥胖')
# elif bmi>28 and bmi<=32:
# 	print('肥胖')
# elif bmi>25 and  bmi<=28:
# 	print('过胖')
# elif bmi>18.5 and bmi<=25:
# 	print('正常')
# else:
# 	print('过轻')

# names=['mi','bob','tracy']
# for name in names:
# 	print(name)

# print(list(range(5)))

# sum=0
# for x in range(5):
# 	sum+=x
# print(sum)

# sum=0
# n=99
# while n>0:
# 	sum+=n
# 	n=n-2
# print(sum)

# n=1
# while n<=100:
# 	if n>10:
# 		break
# 	print(n)
# 	n=n+2
# print('end')
# 	

# d={'michael':95,'bob':74,'tracy':94}
# print(d)
# print(d['michael'])
# print(d.get('michael1'),d.get('michael1',-1))
# d.pop('bob')
# print(d)

# s=set([1,2,3])
# print(s)
# s.add(4)
# print(s)
# s.remove(3)
# print(s)

# s1=set([1,2,3])

# print(s & s1)
# print(s | s1)

# print(abs(100),abs(-20),abs(12.54))
# print(max(1,3,5,8,9))
# print(int('123'),int(12.54),float('12.35'),str(100),bool(1))
# a=abs
# print(a(-1))

# n1=255 #转换成16进制
# print(hex(n1))

# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('bad operand type')
# 	if x>=0:
# 		return x
# 	else:
# 		return -x

# print(my_abs(-88))
# print(my_abs('-88'))

# import math
# def move(x,y,step,angle=0):
# 	nx=x+step*math.cos(angle)
# 	ny=y-step*math.sin(angle)
# 	return nx,ny,5

# x,y,z=move(100,100,60,math.pi/6)
# print(x,y)
# r=move(100,100,60,math.pi/6)
# print(r)

# def power(x,n=2):
# 	s=1
# 	while n>0:
# 		n=n-1
# 		s=s*x
# 	return s

# print(power(5,3),power(5))

# def cale(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# def c(*ns):
# 	sum=0
# 	for x in ns:
# 		sum=sum+x*x
# 	return sum


# print(cale(1,3),cale(1,2,3),c())
# nums=[5,6,7]
# print(c(*nums))

# def pro(*nums):
# 	if len(nums)==0:
# 		raise TypeError('nums is not one')
# 	count=1
# 	for x in nums:
# 		count=count*x
# 	return count

# if pro(5)!=5:
# 	print(pro(5))
# elif pro(5,6)!=30:
# 	print('测试失败!')
# elif pro(5, 6, 7) != 210:
#     print('测试失败!')
# elif pro(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         pro()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


# def fact(n):
# 	if n==1:
# 		return 1
# 	return n*fact(n-1)

# print(fact(5))

# def fact_iter(num,pr):
# 	if num==1:
# 		return pr
# 	return fact_iter(num-1,num*pr)

# print(fact_iter(100,1))

# # 利用递归函数移动汉诺塔:
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)

# move(4, 'A', 'B', 'C')

# l=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print(l[:3],l[2:4],l[-1:])

# st='adbdc'
# print('  hello'[:1])

# def trim(s):
# 	if s[:1]==' ':
# 		s=s[:1]
# 		print(s)
# 		return s[1:]
# 	elif s[-1:]==' ':
# 		le=len(s)
# 		#print(len(s[:le-2]))
# 		s=s[:le-2]
# 		return s[:le-2]
# 	else:
# 		return s

# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败1!')
# elif trim('  hello') != 'hello':
# 	print(trim('  hello'))
#     print('测试失败2!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败3!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败4!')
# elif trim('') != '':
#     print('测试失败5!')
# elif trim('    ') != '':
#     print('测试失败6!')
# else:
#     print('测试成功!')


# d={'a': 1, 'b': 2, 'c': 3}

# for k,v in d.items():
# 	print(k,v)

# for c in 'abc':
# 	print(c)

# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance(123, Iterable))

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

# def findMinAndMax(l):
# 	if(len(l)==0):
# 		return (None,None)
# 	mi=l[0]
# 	ma=l[0]
# 	for x in l:
# 		if mi>x:
# 			mi=x
# 		if ma<x:
# 			ma=x
# 	return (mi,ma)


# print(findMinAndMax([7]))

# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# print([x*x for x in range(1,11)])
# print([x*x for x in range(1,11) if x%2==0])

# print([m+n for m in 'abc' for n in 'xyz'])
# print([m+n for m in range(1,4) for n in range(1,4)])

# import os
# print([d for d in os.listdir('.')])

# L = ['Hello', 'World',18, 'IBM', 'Apple', None]
# print([s.lower() for s in L if isinstance(s,str)])

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# g=fib(6)
# print(g)
# for x in g:
#  	print(x)

# from collections import Iterable
# from collections import Iterator
# print(isinstance([],Iterable))
# print(isinstance([],Iterator))

# def add(x,y,f):
# 	return f(x)+f(y)

# print(add(-5,6,abs))

# def f(x):
# 	return x*x

# r=map(f,[1,2,3,4,5,6])
# print(list(r))

# print(list(map(str,[1,2,3,4,5,6])))

# from functools import reduce
# def fn(x,y):
# 	return x*10+y

# def char2num(s):
# 	digs={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	return digs[s]

# r=reduce(fn,[1,2,3,4,5,6])
# print(r)
# m=map(char2num,'13579')
# # print(list(m))
# r=reduce(fn,m)
# print(r)

# def normalize(name):
# 	return name[:1].lower()+name[1:]

# print(list(map(normalize,['AD','LI','BA'])))


# print(sorted([36,5,-12,9,-21],key=abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# print( sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# def by_name(t):
# 	return t[1]

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_name,reverse=True)
# print(L2)

# def calc_sum(*args):
# 	ax=0
# 	for n in args:
# 		ax=ax+n
# 	return ax

# def lazy_sum(*args):
# 	def sum():
# 		ax=0
# 		for n in args:
# 		    ax=ax+n
# 		return ax
# 	return sum

# print(calc_sum(1,2,3,4))
# print(lazy_sum(1,2,3,4)())

# def createCounter():
# 	def counter(j):
# 		def g():
# 			return j
# 		return g
# 	fs=[]
# 	for i in range(1,5):
# 		fs.append(counter(i))
# 	return fs

# counterA=createCounter()
# print(counterA)
# # print(counterA(),counterA(),counterA())

# l=list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
# print(l)

# f=lambda x:x*x
# print(f(5))

# def build(x,y):
# 	return lambda:x*x+y*y

# print(build(1,2)())

# l=list(filter(lambda n:n%2==1,range(1,20)))
# print(l)


# import functools #它们的__name__已经从原来的'now'变成了'wrapper'

# def log(func):#装饰器
# 	@functools.wraps(func)
# 	def wrapper(*args,**kw):
# 		print('call %s():' % func.__name__)
# 		return func(*args,**kw)
# 	return wrapper

# @log #把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
# def now():
# 	print('2018-3-19')

# print(now.__name__)
# print(log(now))

# import time,functools

# def metric(fn):
# 	@functools.wraps(fn)
# 	def wrapper(*args,**kw):
# 		print('%s executed in %s ms' % (fn.__name__, 10.24))
# 		return fn(*args,**kw)
# 	return wrapper

# @metric
# def fast(x,y):
# 	time.sleep(0.0012)
# 	return x+y

# print(fast(11,22))

# print(int('12345',2))

# import functools
# int2=functools.partial(int,base=2)
# print(int2('12345'))

import test
print(test.greeting('li'))
l=test._private_1('slmao')
print(l)
	
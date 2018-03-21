#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# with open('d:/pythonwork/txt/one.txt','r',encoding='utf-8', errors='ignore') as f:
# 	# print(f.read(4),f.read())
# 	for line in f.readlines():
# 		print(line.strip())# 把末尾的'\n'删掉

# with open('d:/pythonwork/txt/one.txt','w') as f:
# 	f.write('hello,world!')

# with open('d:/pythonwork/txt/one.txt','a',encoding='utf-8') as f:
# 	f.write('hello,world2!')
# 	f.write('测试')
# 	f.writelines('测试换行')
# 	f.writelines('测试换行2')

# import os
# print(os.name)

# print(os.path.abspath('.'))

# filepath=os.path.abspath('.')
# newpath=os.path.join(filepath,'testdir')
# #os.mkdir(newpath)#创建
# #os.rmdir(newpath) #删除

# p='/Users/michael/testdir/file.txt'
# print(os.path.split(p))
# print(os.path.splitext(p))


# l=[x for x in os.listdir('.') if os.path.isdir(x)]
# print(l)

# l=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print(l)


# from datetime import datetime
# import os

# pwd=os.path.abspath('.')


# for f in os.listdir(pwd):
# 	fsize=os.path.getsize(f)
# 	mtime=datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
# 	flag='/' if os.path.isdir(f) else ''
# 	print('%10d  %s  %s%s' % (fsize, mtime, f, flag))


# import pickle
# d=dict(name='bob',age=20,score=88)
# print(pickle.dumps(d))

# with open('d:/pythonwork/txt/one.txt','wb') as f:
# 	pickle.dump(d,f)

# with open('d:/pythonwork/txt/one.txt','rb') as f:
# 	print(pickle.load(f))

# import json
# d=dict(name='bob',age=20,score=88,nice='中国')
# print(json.dumps(d,ensure_ascii=False))

# with open('d:/pythonwork/txt/one.txt','w') as f:
# 	json.dump(d,f)

# with open('d:/pythonwork/txt/one.txt','r') as f:
# 	print(json.load(f))

import json

class Student(object):
	"""docstring for Student"""
	def __init__(self, name,age,score):		
		self.name = name
		self.age=age
		self.score=score

def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

s=Student('bob',20,88)
print(json.dumps(s,default=student2dict))

j=json.dumps(s,default=lambda obj:obj.__dict__)

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

print(json.loads(j,object_hook=dict2student))
s=json.loads(j,object_hook=dict2student)
print(s.name)
import hashlib, hmac

# s='how to use md5 in python hashlib?'.encode('utf-8')
# md5=hashlib.md5()
# md5.update(s)
# print(md5.hexdigest())

# md6=hashlib.md5()
# md6.update('aow to use md5 in '.encode('utf-8'))
# md6.update('python hashlib?'.encode('utf-8'))
# print(md6.hexdigest())

# sha1=hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())

# db={'slmao':'e10adc3949ba59abbe56e057f20f883e'}

# print(db['slmao'])
# def login(user,password):
# 	if db[user]==md5(password):
# 		return True
# 	else:
# 		return False

# def md5(s):
# 	md5=hashlib.md5()
# 	md5.update(s.encode('utf-8'))
# 	return md5.hexdigest()

# if login('slmao','123456'):
# 	print('ok')
# else:
# 	print('err')

# def hmac_md5(s):
# 	return hmac.new('slmao'.encode('utf-8'),s.encode('utf-8'),'MD5').hexdigest()

# print(hmac_md5('123456'))

import itertools
# ns=itertools.count(1)
# for n in ns:
# 	print(n)

# cs=itertools.cycle('ABC')
# for c in cs:
# 	print(c)

# ns=itertools.repeat('A',3)
# for n in ns:
# 	print(n)

# ns=itertools.count(1)
# n=itertools.takewhile(lambda x:x<=10,ns)
# print(list(n))

# for c in itertools.chain('ABC','xyz'):
# 	print(c)

# for key,group in itertools.groupby('AAABABBCCAAda'):
# 	print(key,list(group))

# for key,group in itertools.groupby('AAaBABBCCAAdD',lambda x: x.upper()):
# 	print(key,list(group))

# class Query(object):
# 	"""docstring for Query"""
# 	def __init__(self, name):
# 		self.name = name

# 	def __enter__(self):
# 		print('begin')
# 		return self
# 	def __exit__(self,exc_type,exc_value,traceback):
# 		if exc_type:
# 			print('error')
# 		else:
# 			print('end',exc_type,exc_value)

# 	def query(self):
# 		print('query info about %s...'% self.name)


# with Query('slmao') as q:
# 	q.query()


from contextlib import contextmanager

# class Query(object):
# 	"""docstring for Query"""
# 	def __init__(self, name):
# 		self.name = name

# 	def query(self):
# 		print('query info about %s...'% self.name)

# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
   


# with create_query('slmao') as q:
# 	q.query()

# @contextmanager
# def tag(name):
# 	print('%s'% name)
# 	yield
# 	print('%s'% name)

# with tag('h1'):
# 	print('hello')
# 	print('world')

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as p:
	for line in p:
		print(line)
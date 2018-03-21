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

db={'slmao':'e10adc3949ba59abbe56e057f20f883e'}

print(db['slmao'])
def login(user,password):
	if db[user]==md5(password):
		return True
	else:
		return False

def md5(s):
	md5=hashlib.md5()
	md5.update(s.encode('utf-8'))
	return md5.hexdigest()

if login('slmao','123456'):
	print('ok')
else:
	print('err')

def hmac_md5(s):
	return hmac.new('slmao'.encode('utf-8'),s.encode('utf-8'),'MD5').hexdigest()

print(hmac_md5('123456'))
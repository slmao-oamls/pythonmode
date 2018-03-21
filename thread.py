import time,threading

# def loop():
# 	print('thread %s is running...'% threading.current_thread().name)
# 	n=0
# 	while  n<5:
# 		n=n+1
# 		print('thread %s >>> %s'% (threading.current_thread().name,n))
# 		time.sleep(1)
# 	print('thread %s ended.'% threading.current_thread().name)

# print('thread %s is running...'% threading.current_thread().name)
# t=threading.Thread(target=loop)
# t.start()
# t.join()
# print('thread %s ended.'% threading.current_thread().name)

# balance=0
# lock=threading.Lock()

# def change_it(n):
# 	global balance
# 	balance=balance+n
# 	balance=balance-n

# def run_thread(n):
# 	for i in range(100000):
# 		#先要获取锁
# 		lock.acquire()
# 		try:
# 			change_it(n)
# 		finally:
# 			# 改完了一定要释放锁:
# 			lock.release()
		

# t1=threading.Thread(target=run_thread,args=(5,))
# t2=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print(balance)

import threading

# 创建全局ThreadLocal对象:
local_school=threading.local()

def process_student():
	 # 获取当前线程关联的student:
	std=local_school.student
	print('hello,%s(in %s)'%(std,threading.current_thread().name))

def process_thread(name):
	# 绑定ThreadLocal的student:
	local_school.student=name
	process_student()

t1=threading.Thread(target=process_thread,args=('ali',),name='thread-1')
t2=threading.Thread(target=process_thread,args=('slmao',),name='thread-2')
t1.start()
t2.start()
t1.join()
t2.join()
# from multiprocessing import Process
# import os

# def run_proc(name):
# 	print('Run child Process %s...(%s)'% (name,os.getpid()))

# if __name__=='__main__':
# 	print('parent process %s.'% os.getpid())
# 	p=Process(target=run_proc,args=('test',))
# 	print('child process will start.')
# 	p.start()
# 	#p.join()#通常用于进程间的同步
# 	print('child process end.')

# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
# 	print('Run task %s (%s)...' % (name, os.getpid()))
# 	start=time.time()
# 	time.sleep(random.random()*3)
# 	end=time.time()
# 	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p=Pool(4)#最多同时执行4个进程 默认大小是CPU的核数
# 	for i in range(5):
# 		p.apply_async(long_time_task,args=(i,))
# 	print('waiting for all done...')
# 	p.close()
# 	p.join()
# 	print('all done..')

# import subprocess

# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

# from multiprocessing import Process,Queue
# import os,time,random

# def write(q):
# 	print('process to write %s' % os.getpid())
# 	for v in ['A','B','C','D']:
# 		print('put %s to queue...'% v)
# 		q.put(v)
# 		time.sleep(random.random())

# def read(q):
# 	print('process to read %s'% os.getpid())
# 	while  True:
# 		v=q.get(True)
# 		print('get %s from queue.'% v)


# if __name__=='__main__':
# 	 # 父进程创建Queue，并传给各个子进程：
# 	q=Queue()
# 	pw=Process(target=write,args=(q,))
# 	pr=Process(target=read,args=(q,))
# 	 # 启动子进程pw，写入:
# 	pw.start()
# 	 # 启动子进程pr，读取:
# 	pr.start()
#      # 等待pw结束:
# 	pw.join()
# 	 # pr进程里是死循环，无法等待其结束，只能强行终止:
# 	pr.terminate()

# print(__file__)
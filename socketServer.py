import socket,time,threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999))

s.listen(5)
print('waiting for connection...')


def tcplink(sock,addr):
	print('accept new con from %s:%s'% addr)
	sock.send(b'welcome!')
	while 1:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('hello,%s!'%data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('con from %s:%s closed'% addr)

while 1:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
		
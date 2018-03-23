
# def consumer():
# 	rx=''
# 	while 1:
# 		n=yield rx
# 		if not n:
# 			return
# 		print('[c] consuming %s...'% n)
# 		rx='200 ok %s'% n

# def produce(c):
# 	c.send(None)
# 	n=0
# 	while n<5:
# 		n=n+1
# 		print('[p] producing %s...'% n)
# 		r1=c.send(n)
# 		print('[p] consumer return:%s'% r1)
# 	c.close()


# c=consumer()
# produce(c)

# 首先调用c.send(None)启动生成器；

# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

# consumer通过yield拿到消息，处理，又通过yield把结果传回；

# produce拿到consumer处理的结果，继续生产下一条消息；

# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

# import asyncio,threading

# @asyncio.coroutine
# def hello():
# 	print('hello,world!')
# 	r=yield from asyncio.sleep(1)
# 	print('hello again!%s'% r)


# loop=asyncio.get_event_loop()

# loop.run_until_complete(hello())
# loop.close()

#等同上面代码 async=@asyncio.coroutine await=yield from
# async def hello():
# 	print('hello,world!')
# 	r=await asyncio.sleep(1)
# 	print('hello again!%s'% r)

# loop=asyncio.get_event_loop()

# loop.run_until_complete(hello())
# loop.close()

# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())


# loop=asyncio.get_event_loop()
# tasks=[hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# @asyncio.coroutine
# def wget(host):
# 	print('wget:%s...'% host)
# 	connect=asyncio.open_connection(host,80)
# 	reader,writer=yield from connect
# 	header='GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
# 	writer.write(header.encode('utf-8'))
# 	yield from writer.drain()
# 	while  1:
# 		line=yield from reader.readline()
# 		if line==b'\r\n':
# 			break
# 		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
# 	writer.close()


# async def wget(host):
# 	print('wget:%s...'% host)
# 	connect=asyncio.open_connection(host,80)
# 	reader,writer=await connect
# 	header='GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
# 	writer.write(header.encode('utf-8'))
# 	await writer.drain()
# 	while  1:
# 		line=await reader.readline()
# 		if line==b'\r\n':
# 			break
# 		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
# 	writer.close()


# loop=asyncio.get_event_loop()
# tasks=[wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

import asyncio
from aiohttp import web

async def index(request):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>index</h1>')
async def hello(request):
	await asyncio.sleep(0.5)
	text='<h1>hello, %s!</h1>' % request.match_info['name']
	return web.Response(body=text.encode('utf-8'))

async def init(loop):
	app=web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	app.router.add_route('GET','/hello/{name}',hello)
	srv=await loop.create_server(app.make_handler(),'127.0.0.1',8000)
	print('Server started at http://127.0.0.1:8000...')
	return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
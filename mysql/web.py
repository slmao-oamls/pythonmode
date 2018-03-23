

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body='<h1>hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return  [body.encode('utf-8')]   #[b'<h1>hello,web!</h1>']


from wsgiref.simple_server import make_server

httpd=make_server('',8000,application)
print('serving http on port 8000...')

httpd.serve_forever()

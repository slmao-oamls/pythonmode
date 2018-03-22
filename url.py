# from urllib import request

# url='https://api.douban.com/v2/book/2129650'
# with request.urlopen(url) as f:
# 	data=f.read()
# 	print('status:', f.status,f.reason)
# 	for k,v in f.getheaders():
# 		print('%s:%s'%(k,v))
# 	print('date:',data.decode('utf-8'))

# req=request.Request('http://www.douban.com/')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data=f.read()
#     print('status:', f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('date:',data.decode('utf-8'))

# from urllib import request, parse

# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])

# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# from urllib import request
# import json

# def fetch_data(url):
#     with request.urlopen(url) as f:
#         data1=f.read()
#         return json.loads(data1.decode('utf-8'))
     
# url='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
# data=fetch_data(url)
# print(data)
# print(data['query']['count'])
# print(data['query']['results']['channel']['location']['city'])


from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self,tag,attrs):
        print('<%s>'% tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)
        

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


		
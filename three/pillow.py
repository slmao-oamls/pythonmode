# from PIL import Image,ImageFilter,ImageFont,ImageDraw

# im=Image.open('icon.png')

# w,h=im.size

# print('original image size:%sX%s'%(w,h))

# im.thumbnail((w//2,h//2))
# print('resize image to :%sX%s'%(w//2,h//2))

# im.save('thumbnail.png','png')

# im2=im.filter(ImageFilter.BLUR)
# im2.save('cut/blur.png','png')


# import random

# codestr=''

# def rndChar():
# 	return chr(random.randint(65,90))

# def rndColor():
# 	return (random.randint(64,255),random.randint(64, 255), random.randint(64, 255))

# def rndColor2():
# 	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# width=60*4
# height=60
# image=Image.new('RGB',(width,height),(255,255,255))

# font=ImageFont.truetype('Arial.ttf',36)

# draw=ImageDraw.Draw(image)

# for x in range(width):
# 	for y in range(height):
# 		draw.point((x,y),fill=rndColor())

# for t in range(4):
# 	s=rndChar()
# 	codestr=codestr+s
# 	draw.text((60*t+10,10),s,font=font,fill=rndColor2())

# image2=image.filter(ImageFilter.BLUR)
# image2.save('cut/code.jpg','jpeg')
# print(codestr)


# import requests
# r=requests.get('https://www.douban.com/')
# print(r.status_code,r.text)

# r=requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
# print(r.url,r.status_code)

# r=requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r.status_code,r.headers['Content-Type'])
# print(r.cookies)

# import chardet

# print(chardet.detect(b'hello,world!'))

# data = '离离原上草，一岁一枯荣'.encode('gbk')
# print(chardet.detect(data))

# from tkinter import *

# class Application(Frame):
# 	"""docstring for Application"""
# 	def __init__(self, master=None):
# 		Frame.__init__(self,master)

# 		self.pack()
# 		self.createWidgets()

# 	def createWidgets(self):
# 		self.helloLabel=Label(self,text='hello,world!')
# 		self.helloLabel.pack()
# 		self.quitButton=Button(self,text='Quit',command=self.quit)
# 		self.quitButton.pack()

# app=Application()

# app.master.title('hehe')

# app.mainloop()
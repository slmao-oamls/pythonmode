from flask import Flask 
from flask import request,render_template

app=Flask(__name__)

# @app.route('/',methods=['GET','POST'])
# def home():
# 	return '<h1>home</h1>'

# @app.route('/signin',methods=['GET'])
# def signin_from():
# 	return '''<form action="/signin" method="post">
# 			<p><input name="username"></p>
# 			<p><input name="password" type="password"></p>
# 			<p><button type="submit">提交</button></p>
# 			</form>'''

# @app.route('/signin',methods=['POST'])
# def signin_do():
# 	if request.form['username']=='admin' and request.form['password']=='password':
# 		return '<h3>hello,admin!</h3>'
# 	return '<h3>用户名或密码错误</h3>'

@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_from():
	return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin_do():
	username=request.form['username']
	password=request.form['password']
	if username=='admin' and password=='password':
		return render_template('signin-ok.html',username=username)
	return render_template('form.html',message='用户名或密码错误',username=username)

if __name__=='__main__':
	app.run()
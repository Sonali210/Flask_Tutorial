from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home_page():
	return 'This is home page'

@app.route('/admin')
def hello_admin():
	return 'Hello admin'


@app.route('/guest/<string:guest>')
def hello_guest(guest):
	return ' Hello %s' %guest

@app.route('/user/<name>')
def hello_user(name):
	if name=='admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest', guest=name))

if __name__ == "__main__":
    app.run(debug=True, port='2121')
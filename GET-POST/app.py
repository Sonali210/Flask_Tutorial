from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)



@app.route('/success/<name>')
def success(name):
	return 'hey %s, We used POST method to send data to URL' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		user= request.form['nm']
		return redirect(url_for('success', name=user))
	else:
		user= request.args.get('nm')
		return redirect(url_for('success', name=user))



@app.route('/')
def index():
	return render_template('get.html')


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
form flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://sql10367306:b2Lr6QMYap@sql10.freemysqlhosting.net/sql10367306'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

db = SQLAlchemy(app)

class Commnents(db.Model):
	id = db.Column(db.Interger, primary_key=True)
	name =  db.Column(db.String(40))
	Commnent = db.Column(db.String(1000))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	return render_template('index.html', name=name, comment=comment)

@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)

if __name__ == '__main__':
	app.run(debug=True)
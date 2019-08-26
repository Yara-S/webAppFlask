from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def ola():
	# index.html follows jinja template
	name = 'Mariana'
	subjects = ["História", "Ingles", "Biologia"]
	return  render_template("index.html", user_name = name, subjects = subjects)
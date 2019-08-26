from flask import Flask, redirect
from flask import render_template

app = Flask(__name__)

@app.route("/")
def ola():
	# index.html follows jinja template
	name = 'Mariana'
	subjects = ["História", "Ingles", "Biologia", "Física"]
	return  render_template("index.html", user_name = name, subjects = subjects)

@app.route("/subject/<subject_name>")
def subject(subject_name):
	if (subject_name == "Biologia"):
		return redirect("https://www.mcb.harvard.edu/")
	elif (subject_name == "Ingles"):
		return render_template(subject_name + ".html")
	else:
		return render_template( "defaultSubject.html", subject_name=subject_name)
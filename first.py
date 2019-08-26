from flask import Flask
from flask import render_template_string #to combine html with python code

app = Flask(__name__)

#defining the route
@app.route("/")
def ola():
	name = "Joyce" #could have been a query result from DB

	#putting a for loop in html
	html = """ 
				<html>
					<h1> Olá, {{user_name}} , bem vinda a nossa página! </h1>

					{% for subject in subjects %}
						<li> {{subject}} </li>
					{% endfor %}
				</html>
			"""
	subjects = ["Matemática", "Física", "Ingles"]
	rendered_html = render_template_string(html, user_name = name, subjects = subjects)

	return rendered_html
from flask import Flask, render_template
from search import cybersecurity_keywords, terrorism_keywords, multi_search

app = Flask(__name__)

@app.route("/")
def home():
	return render_template(
		'home.html',
		font_url='https://fonts.googleapis.com/css?family=Roboto'
		)
	
@app.route("/about")
def about():
    return render_template(
		"about.html",
		font_url='https://fonts.googleapis.com/css?family=Roboto'
		)

@app.route("/cybersecurity")
def cybersecurity():
	words = cybersecurity_keywords()
	results = multi_search(words)
	return render_template(
		'cybersecurity.html',
		results=results,
		font_url='https://fonts.googleapis.com/css?family=Roboto'
		)

@app.route("/terrorism")
def terrorism():
	words = terrorism_keywords()
	results = multi_search(words)
	return render_template(
		'terrorism.html',
		results=results,
		font_url='https://fonts.googleapis.com/css?family=Roboto'
		)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
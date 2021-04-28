from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')


#def index():
#	return "<h1>My First WebPage Use Flask in 2020-04-26</h1>"

def index():
	index_name = "raiden"
	stuff = "This is bold text"
	favorite_cars = ['rs3','gti','evo','sti','a45','nissan_gtr']
	return render_template("index.html",first_name = index_name,stuff =stuff,favorite_cars = favorite_cars)


@app.route('/users/<names>')

def users(names):
	return render_template("users.html",user_name = names)
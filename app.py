# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Anmol Singh" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    return "Hi Father"

# define the route to mother webpage
@app.route("/mother")
def father():
    return "Hi mother"

# define the route to friends webpage
@app.route("/friend")
def father():
    return "Hi friend"

# add other routes, if you want
@app.route("/teacher")
def father():
    return "Hi teacher"



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

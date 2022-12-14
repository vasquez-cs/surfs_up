##From the lesson module     
#1. import flask
from flask import Flask

#2 Define what to do when a user goes to the index route
app = Flask(__name__)

#3 define what to do when a user goes to the index route
@app.route("/")
def hello_world():
        return "Hello World"

#4 Define what to do when a user goes to the /about route
@app.route("/about")
def about():
    print("Sever received a request for 'About' page")
    return "Welcome to my 'About' page!"

if __name__ == "__main__":
    app.run(debug=True)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
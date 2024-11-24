from flask import Flask,request
from flask import render_template

myApp=Flask(__name__)

@myApp.route('/')
def index():
    return render_template("index.html")

@myApp.route("/farToCel")
def farToCel():
    far=float(request.args['far'])
    cel =(far - 32) * 5/9
    return f"<h1>far={far} is same as cel={cel}</h1>"

@myApp.route("/celToFar")
def celToFar():
    cel=float(request.args['cel'])
    far = (cel * 9/5) + 32
    return f"<h1>cel={cel} is same as far={far}</h1>"

if __name__=='__main__':
    myApp.run(debug=True)
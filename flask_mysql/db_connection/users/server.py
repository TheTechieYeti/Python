from flask import Flask, render_template, request, session, redirect
from user import User
app = Flask(__name__)  
app.secret_key ='testsecretkey'

@app.route('/')         
def index():
    users = User.get_all()
    return render_template("index.html", users=users)

@app.route('/new')         
def new():
    return render_template("new.html")

@app.route('/process', methods = ["POST"])         
def process():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect('/')


@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    
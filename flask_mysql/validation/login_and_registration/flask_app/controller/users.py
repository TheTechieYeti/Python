from flask_app import app
from flask import render_template, redirect, session, flash, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
from flask_app.model import validate, user
bcrypt = Bcrypt(app)
@app.route('/')         
def index():

    return render_template("index.html")

@app.route('/register', methods = ["POST"])         
def create():
    if not validate.validate_user(request.form):
        return redirect('/')
    elif not validate.validate_email(request.form):
        return redirect('/')
    elif not validate.validate_password(request.form):
        return redirect('/')
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    session['user_id'] = user.User.create_user(data)
    # print(f"My variable this_user is {this_user}")
    # session['user_id'] = user.User(data)
    return redirect(f'/dashboard/{session["user_id"]}')

@app.route("/dashboard/<id>")     
def dashboard(id):
    if not session:
        flash("You must be logged to view the previous page.")
        return redirect ('/')
    one_user = user.User.get_one_user(session['user_id'])
    return render_template("user.html", user=one_user) 

@app.route('/logout')         
def logout():
    session.pop('user_id')
    print(f'Test to see if there is any information in session{session}')
    return redirect ("/")

@app.route('/login', methods = ["POST"])         
def user_login():
    data = {
        "email":request.form['email']
    }
    user_in_db = user.User.get_user_by_email(data)
    if not user_in_db:
        flash("Please check your email address. No user found with that email address.")
        return redirect ("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid password")
        return redirect ('/')
    session['user_id'] = user_in_db.id
    return redirect(f"dashboard/{session['user_id']}")
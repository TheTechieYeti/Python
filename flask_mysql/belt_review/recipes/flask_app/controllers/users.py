from flask_app import app
from flask import render_template, redirect, session, flash, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
from flask_app.model import user, recipe
bcrypt = Bcrypt(app)

@app.route('/')         
def index():

    return render_template("index.html")

@app.route('/register', methods=["POST"])         
def register():
    if not user.validate_user(request.form):
        return redirect ('/')
    if not user.validate_email(request.form):
        return redirect ('/')
    if not user.validate_password(request.form):
        return redirect ('/')
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash(request.form["password"]),
    }
    session['user_id'] = user.User.create_user(data)
    return redirect("/dashboard")

@app.route('/dashboard')         
def dashboard():
    print(session)
    if not session:
        flash('You must be logged in to view this page')
        return redirect('/')
    one_user_id = session["user_id"]
    return render_template("dashboard.html", user=user.User.get_logged_in_user(one_user_id), recipes=recipe.Recipe.get_all_recipies())

@app.route('/login', methods = ["POST"])         
def login():
    data = {
        "email" : request.form["email"],
    }
    print(f'this is my data from my request form {data}')
    login_user = user.User.get_user_by_email(data)
    if not login_user:
        flash("Please check your email address. No user found with that email address.")
        return redirect ("/")
    if not bcrypt.check_password_hash(login_user.password, request.form["password"]):
        flash("Incorrect Password")
        return redirect ("/")
    session["user_id"] = login_user.id
    return redirect("/dashboard",) 

@app.route('/logout')         
def logout():
    session.pop('user_id')
    return redirect("/")
from flask_app import app 
from flask import render_template, redirect, request
from flask_app.model import email
from flask_app.config.mysqlconnection import connectToMySQL
@app.route('/')         
def emails():

    return render_template("email.html")

@app.route('/create', methods = ["POST"])         
def create_email():
    if not email.Email.validate_email(request.form):
        return redirect ('/')
    data = {
        "email" : request.form["email"]
    }
    email.Email.create(data)
    return redirect("/success")

@app.route('/success')         
def success():  
    return render_template("success.html", emails = email.Email.get_all_email())

@app.route('/destroy/<int:id>')         
def destroy(id):
    data = {
        "id" : id
    }
    email.Email.delete(data)
    return redirect("/success")
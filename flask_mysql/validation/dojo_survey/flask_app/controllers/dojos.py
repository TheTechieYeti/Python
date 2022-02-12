from flask_app import app 
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import dojo
@app.route('/')         
def index():
    return render_template("test_form.html")

@app.route('/submit', methods=["POST"])         
def submit():
    print(request.form)
    if not dojo.Dojo.validate_dojo(request.form):
        return redirect("/")
    data = {
    "name" : request.form["name"],
    "location" : request.form["dojo_location"],
    "language" : request.form["favorite_language"],
    "comment" : request.form["comments"]
    }
    new_dojo_id = dojo.Dojo.dojo_create(data)
    print(new_dojo_id)
    return redirect(f'/display/{new_dojo_id}',)

@app.route('/display/<int:id>')         
def display(id):
    data = {
        "id": id
    }
    return render_template("display.html", dojo = dojo.Dojo.get_one_dojo(data))

@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')


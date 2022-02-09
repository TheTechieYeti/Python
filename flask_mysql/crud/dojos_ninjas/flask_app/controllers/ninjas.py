from flask_app import app 
from flask import render_template, request, redirect
# from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja 

@app.route('/ninjas')         
def index():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)

@app.route('/ninjas/create', methods=["POST"])         
def create_ninja():
    print(f"This should be an integer for my dojo id {request.form['dojo_id']}")
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'age': request.form['age'],
        'first_name': request.form['fname'],
        'dojos_id' : request.form['dojo_id']
    }
    new_ninja = Ninja.save(data)
    print(f'Successfuly saved this information {new_ninja}')
    return redirect("/dojos")
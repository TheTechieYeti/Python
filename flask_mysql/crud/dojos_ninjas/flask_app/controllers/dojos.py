from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route('/dojos')         
def dojos():
    dojos = Dojo.get_all() 
    
    return render_template("dojos.html", dojos = dojos)

@app.route('/dojos/<int:dojoid>')
def dojo(dojoid):
    data = {
        "id":dojoid
    }
    dojo_from_database = Dojo.get_dojo_with_ninjas(data)
    
    return render_template("dojo.html", dojo=dojo_from_database)

@app.route('/dojos/create', methods=["POST"])
def createdojo():
    data = {
        "name": request.form["dojo_name"]
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')
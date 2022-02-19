from flask_app import app
from flask import render_template, redirect, session, flash, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.model import user, recipe

@app.route('/recipes/new', )         
def new_recipe():
    if not session['user_id']:
        flash('You must be logged in to view this page')
        return redirect ('/')
    return render_template("new_recipe.html")

@app.route('/recipes/new/create', methods=["POST"])         
def create_recipe():
    data={
        "users_id" : session['user_id'],
        "name" : request.form["name"],
        "description" : request.form["description"],
        "directions" : request.form["directions"],
        "made" : request.form["made"],
        "under_30" : int(request.form["under_30"]),

    }
    recipe_id = recipe.Recipe.create_new_recipe(data)
    print(f"this is my recipe id {recipe_id}")
    return redirect(f"/recipes/{recipe_id}")

@app.route('/recipes/<int:recipe_id>')         
def one_recipe(recipe_id):
    if not session:
        flash('You must be logged in to view this page')
        return redirect ('/')
    this_recipe_id = recipe_id
    print(f'this is my recipe id {this_recipe_id}')
    return render_template("recipe.html", recipe = recipe.Recipe.get_one_recipe(this_recipe_id), user=user.User.get_one_user(session["user_id"]))

@app.route('/recipes/edit/<int:recipe_id>')         
def edit_recipe(recipe_id):
    if not session:
        flash('You must be logged in to view this page')
        return redirect ('/')
    return render_template("edit_recipe.html", recipe=recipe.Recipe.get_one_recipe(recipe_id))

@app.route('/recipes/update', methods = ["POST"])
def update_recipe():
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect (f'/recipes/edit/{request.form["id"]}')
    data={
        "id" : int(request.form['id']),
        "users_id" : session['user_id'],
        "name" : request.form["name"],
        "description" : request.form["description"],
        "directions" : request.form["directions"],
        "made" : request.form["made"],
        "under_30" : request.form["under_30"],

    }
    recipe.Recipe.update_recipe_by_id(data)
    return redirect (f'/recipes/{request.form["id"]}')

@app.route('/recipes/delete/<int:id>')         
def destroy(id):
    if not session:
        flash('You must be logged in to view this page')
        return redirect ('/')
    query = "DELETE * FROM recipes where id = %(id)s;"
    MySQLConnection(db).query_db(query, id)
    return redirect("/dashboard")

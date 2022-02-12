from flask_app import app
from flask import render_template, redirect, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.model import user, friendship
@app.route('/')         
def index():

    return redirect("friendships")
@app.route('/friendships')         
def friendships():
    users = user.User.get_everything()
    friendships = friendship.Friendship.get_all_friendships()
    return render_template("friendships.html", users=users, friendships=friendships)

@app.route('/user/create', methods = ["POST"])         
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    user.User.user_create(data)
    return redirect ("/friendships")

@app.route('/friendships/create', methods = ["POST"])         
def create_friendship():
    data = {
        "user_id": request.form['user_id'],
        "friend_id": request.form['friend_id']
    }
    user.User.friendship_create(data)
    return redirect("/friendships")
from flask_app import app
from flask import render_template, redirect, session, flash, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
from flask_app.model import user, message

@app.route('/create_message', methods = ["POST"])         
def new_message():
    data = {
        "user_id" : request.form["user_id"],
        "receiver_id" : request.form["receiver_id"],
        "content" : request.form["content"],
    }
    message.Message.create_message(data)
    return redirect ("/dashboard")

from flask_app import app
from flask import render_template, redirect, session, flash, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
from flask_app.model import user, event
import os
from werkzeug.utils import secure_filename
bcrypt = Bcrypt(app)

UPLOAD_FOLDER = 'C:/Users/Yeti/Documents/Coding_Dojo/Python/projects/iSport/flask_app/static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/user/<int:user_id>/upload_img', methods=['GET', 'POST'])
def upload_file(user_id):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(f'/user/{user_id}')
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(f'/user/{user_id}')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = {
                "id" : user_id,
                "img_path" : f"images/{filename}"
            }
            print(f'This is my image data {data}')
            user.User.upload_image(data)
            return redirect(f'/user/{user_id}')
@app.route('/')         
def log_reg():

    return render_template("login_registration.html")

@app.route('/register', methods=["POST"])         
def register():
    if not user.User.validate_user(request.form):
        return redirect ('/')
    if not user.User.validate_email(request.form):
        return redirect ('/')
    if not user.User.validate_password(request.form):
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
    if 'user_id' not in session:
        flash('You must be logged in to view this page')
        return redirect('/')
    
    return render_template("dashboard.html", user = user.User.get_logged_in_user(), events=event.Event.get_all_events_with_creator_attendees())

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

@app.route('/user/<int:user_id>')          
def display_account(user_id):
    if 'user_id' not in session:
        flash('You must be logged in to view this page')
        return redirect('/')
    
    return render_template("user.html", user=user.User.get_logged_in_user(),events=event.Event.get_all_events_with_creator_attendees(), profile_user=user.User.get_one_user(user_id))

@app.route('/user/<int:user_id>/edit')          
def edit_user(user_id):
    if 'user_id' not in session:
        flash('You must be logged in to view this page')
        return redirect('/')
    
    return render_template("user_edit.html", user=user.User.get_logged_in_user())

@app.route('/user/<int:user_id>/edit/process', methods = ["POST"])         
def update_user(user_id):
    print(request.form)
    if not user.User.validate_user(request.form):
        return redirect (f'/user/{user_id}/edit')
    if not user.User.validate_email(request.form):
        return redirect (f'/user/{user_id}/edit')
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "id" : user_id
    }
    user.User.update_user(data)
    return redirect(f"/user/{user_id}")
@app.route('/logout')         
def logout():
    session.pop('user_id')
    return redirect("/")
    
from flask import Flask, render_template, request, session, redirect
from user import User
app = Flask(__name__)  
app.secret_key ='testsecretkey'

@app.route('/users')         
def index():
    users = User.get_all()
    return render_template("index.html", users=users)

@app.route('/users/new')         
def new():
    return render_template("new.html")

@app.route('/users/new/process', methods = ["POST"])         
def process():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    userid = User.save(data)  ###Why does this store my user id? Why is the return value of User.save(data) the user id? 
    print(f"process test {userid}")
    return redirect(f'/users/{userid}')

@app.route('/users/<int:userid>')
def show(userid):
    data ={
        "id": userid
    }
    user_from_database = User.get_one(data)
    print(f"DB USER: {user_from_database}")
    print(type(user_from_database))
    return render_template("user.html", user=user_from_database)

@app.route('/users/<int:userid>/edit')         
def edit(userid): ## Our id from the browser gets passed into our function as a parameter
    data ={
        "id":userid  # key of id = value from our browser.
    }
    user_from_database = User.get_one(data) ## This variable equals the value of the class method we called. The class method returned value is one instantiation of a User class that has all the attributes of the corresponding tables from our data base. 
    print(f"DB USER: {user_from_database}")
    print(type(user_from_database))
    return render_template("edit.html", user=user_from_database) ## This is returning the our instance of User Class as a variable 'user'

@app.route('/users/<int:userid>/edit/update', methods=["POST"])         
def editupdate(userid):
    data = {
        "id": userid,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    print(f"This is the data to be updated {data}")
    User.update(data)
    return redirect('/users')

@app.route('/users/<int:userid>/delete')         
def delete(userid):
    data = {
        "id": userid,
    }
    print(f"User {data} is about to be deleted.")
    User.delete(data)
    return redirect('/users')

@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    
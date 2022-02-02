from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html")  # Return the string 'Hello World!' as a response
@app.route('/users')
def users_table():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('lists.html', users = users)

# @app.route('/lists')
# def render_lists():
#     # Soon enough, we'll get data from a database, but for now, we're hard coding data
#     student_info = [
#     {'name' : 'Michael', 'age' : 35},
#     {'name' : 'John', 'age' : 30 },
#     {'name' : 'Mark', 'age' : 25},
#     {'name' : 'KB', 'age' : 27}
#     ]
#     return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


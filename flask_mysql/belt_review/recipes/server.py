from flask_app import app
from flask import session
from flask_app.controllers import recipes, users
if __name__=="__main__":   
    app.run(debug=True)  
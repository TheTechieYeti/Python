from flask_app import app  #from the folder flask_app import app. App is actually from __init__.py
from flask_app.controllers import dojos, ninjas


if __name__=="__main__":   
    app.run(debug=True) 
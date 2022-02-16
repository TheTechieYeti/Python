from flask import flash, session
import re
from flask_app.config.mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
db = "login_schema"
@staticmethod
def validate_email(email):
    is_valid = True
    if len(email['email']) == 0:
        is_valid = False
        flash("you must enter an email address!")
        return is_valid
    if not EMAIL_REGEX.match(email['email']):
        flash("Invalid email address!")
        is_valid = False
        return is_valid
    query = "SELECT * FROM users WHERE email = %(email)s;"
    result = connectToMySQL(db).query_db(query, email)
    print(result)
    if len(result) >= 1:
        flash("Email Already Taken!")
        is_valid=False
    if not EMAIL_REGEX.match(email['email']):
        flash("Email is not valid!")
        is_valid = False
    return is_valid
@staticmethod
def validate_user(user):
    is_valid = True
    if not user['first_name']:
        flash("Please enter a first name")
        is_valid = False
    elif len(user['first_name']) < 2:
        flash("First must be at least 2 characters.")
        is_valid = False
    if not user['last_name']:
        flash("Please enter a last name")
        is_valid = False
    elif len(user['last_name']) < 3:
        flash("Last name must be at least 3 characters.")
        is_valid = False
    return is_valid
@staticmethod
def validate_password(user):
    is_valid = True
    if not user['password']: #checks to make sure the user input something
        is_valid = False
        flash("Please enter a password that contains one letter, one number, and is a least 8 characters.")
    elif len(user['password']) < 8: #checks to make sure the user input at least 8 characters
        is_valid = False
        flash("Please enter a password that is AT LEAST 8 characters and contains one letter and one number.")
    if re.match('^[a-zA-Z]*$', user['password']): #checks if it is all letters
        is_valid = False
        flash("Please enter a password that contains ONE NUMBER, one letter, and is at least 8 characters long.")
    if re.match('^[0-9]*$', user['password']): #checks if it is all numbers
        is_valid = False
        flash("Please enter a password that contains ONE LETTER, one number and is at least 8 characters long.")
    if not user['confirm_password']: #checks to see if user input confirm password
        is_valid = False
        flash("Please confirm your password")
    elif user['confirm_password'] != user['password']: #if user did input confirm password, checks to see if it is the same as password
        is_valid = False
        flash("Passwords do not match. Please re-enter")
    return is_valid
        
    
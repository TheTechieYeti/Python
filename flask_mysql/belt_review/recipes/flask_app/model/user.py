from flask_app import app 
from flask_app.config.mysqlconnection import MySQLConnection
from flask import session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
db="recipes_schema"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []
    
    @classmethod
    def get_logged_in_user(cls, data):
        data = {
            "id" : session["user_id"]
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        this_user = cls(MySQLConnection(db).query_db(query, data)[0])
        # query_message = "SELECT * FROM messages WHERE user_id = users.id "
        return this_user

    @classmethod
    def get_one_user(cls, data):
        data1 = {
            "id" : data
        }
        print(f'This is my data from my get_one_user {data1}')
        query = "SELECT * FROM users WHERE id = %(id)s;"
        this_user_data = MySQLConnection(db).query_db(query, data1)
        this_user = cls(this_user_data[0])
        # query_message = "SELECT * FROM messages WHERE user_id = users.id "
        return this_user

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        all_users = []
        for i in MySQLConnection(db).query_db(query):
            all_users.append(cls(i))
        return all_users
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user = MySQLConnection(db).query_db(query, data)
        print(f'My query is returning as {user}')
        return user
    
    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        this_user_info = MySQLConnection(db).query_db(query,data)
        if len(this_user_info) < 1:
            return False
        this_user = cls(this_user_info[0])
        return this_user

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
    result = MySQLConnection(db).query_db(query, email)
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
    elif len(user['first_name']) < 3:
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
        flash("Please enter a password that contains one letter, one number, and is a least 8 characters and confirm it.")
    elif len(user['password']) < 8: #checks to make sure the user input at least 8 characters
        is_valid = False
        flash("Please enter a password that is AT LEAST 8 characters and contains one letter and one number.")
    elif re.match('^[a-zA-Z]*$', user['password']): #checks if it is all letters
        is_valid = False
        flash("Please enter a password that contains ONE NUMBER, one letter, and is at least 8 characters long.")
    elif re.match('^[0-9]*$', user['password']): #checks if it is all numbers
        is_valid = False
        flash("Please enter a password that contains ONE LETTER, one number and is at least 8 characters long.")
    elif not user['confirm_password']: #checks to see if user input confirm password
        is_valid = False
        flash("Please confirm your password")
    elif user['confirm_password'] != user['password']: #if user did input confirm password, checks to see if it is the same as password
        is_valid = False
        flash("Passwords do not match. Please re-enter")
    return is_valid


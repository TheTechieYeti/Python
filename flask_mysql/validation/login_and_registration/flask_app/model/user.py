from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection
from flask import session
db = "login_schema"
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user = MySQLConnection(db).query_db(query, data)
        print(f'My query is returning as {user}')
        return user
    
    @classmethod
    def get_one_user(cls, data):
        data = {
            "id" : session['user_id']
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        return cls(MySQLConnection(db).query_db(query, data)[0])
    
    @classmethod
    def get_user_by_email(cls, data):
        print(data)
        query = "SELECT * FROM users WHERE email = %(email)s;"
        this_user = MySQLConnection(db).query_db(query, data) 
        print(f'this is the length of my query {this_user}')
        print(f'This is the type of data my query is {type(this_user)}')
        if len(this_user) < 1:
            return False
        return cls(this_user[0])
    
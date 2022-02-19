from tkinter.messagebox import NO
from flask_app import app 
from flask_app.config.mysqlconnection import MySQLConnection
from flask import session, flash
from flask_app.model import user
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
db="recipes_schema"

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.users_id = data['users_id']
        self.name = data['name']
        self.description = data['description']
        self.directions = data['directions']
        self.made = data['made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
    def true_false(self):
        if self.under_30 == 0:
            return 'No'
        return 'Yes'

    @classmethod
    def create_new_recipe(cls,data):
        print(data)
        query = "INSERT INTO recipes (users_id, name, description, directions, made, under_30) VALUES(%(users_id)s,%(name)s,%(description)s,%(directions)s,%(made)s,%(under_30)s); "
        return MySQLConnection(db).query_db(query, data)
    @classmethod
    def get_one_recipe(cls,data):
        data1= {
            "id":data
        }
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        return cls(MySQLConnection(db).query_db(query, data1)[0])
    @classmethod
    def update_recipe_by_id(cls,data):
        print(data)
        query = "UPDATE recipes SET name = %(name)s, description=%(description)s, directions=%(directions)s, made=%(made)s, under_30=%(under_30)s WHERE id = %(id)s;"
        return MySQLConnection(db).query_db(query, data)
    @classmethod
    def get_all_recipies(cls):
        query="SELECT * FROM recipes JOIN users ON users_id = users.id;"
        recipes = []
        for row in MySQLConnection(db).query_db(query):
            print(row)
            this_recipe = cls(row)
            user_info = {
                "id" : row['users.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at']
            }
            this_recipe.user = user.User(user_info)
            print(f'this is my user to be associate with my recipe {this_recipe.user}')
            recipes.append(this_recipe)
        print(recipes)
        return recipes
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if not recipe['name']:
            flash("Please enter a recipe name")
            is_valid = False
        elif len(recipe['name']) < 4:
            flash("Recipe name must be at least 3 characers")
            is_valid = False
        if not recipe['description']:
            flash("Please enter description")
            is_valid = False
        elif len(recipe['description']) < 4:
            flash("Description must be at least 3 characters")
            is_valid = False
        if not recipe['directions']:
            flash("Please enter directions")
            is_valid = False
        elif len(recipe['directions']) < 4:
            flash("Directions must be at least 3 characters")
            is_valid = False
        if not recipe['made']:
            flash("Please enter the date you last made this dish")
            is_valid = False
        
        return is_valid
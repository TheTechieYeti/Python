from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

db = "dojo_survery_schema"
class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def dojo_create(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES(%(name)s,%(location)s,%(language)s,%(comment)s);"
        return MySQLConnection(db).query_db(query, data)

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos where id = %(id)s;"
        return cls(MySQLConnection(db).query_db(query, data)[0])

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if not dojo['name']:
            flash("Name must be at least 3 characters.")
            is_valid = False
        elif len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['dojo_location']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['favorite_language']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if not len(dojo['comments']):
            flash("Comment must be at least 1 character.")
            is_valid = False
        return is_valid
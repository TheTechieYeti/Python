from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import datetime, re
db = "emails_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    # def time_format(self):
    #     self.updated_at = datetime.strftime(self.updated_at, "%-m/%-d/%Y %-I %p")

    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        connectToMySQL(db).query_db(query, data)
        return 
    

    @classmethod
    def get_all_email(cls):
        query = "SELECT * FROM emails;"
        all_emails = []
        results = connectToMySQL(db).query_db(query)

        for i in results:
            data = {
                "id": i["id"],
                "email": i["email"],
                "created_at": i["created_at"],
                "updated_at": i["updated_at"],
            }
            print(data)
            one_email= cls(data)
            print(one_email.id)
            # one_email.time_format()
            all_emails.append(one_email)
            
        return all_emails
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        print(connectToMySQL(db).query_db(query, data))
        return 
    @staticmethod
    def validate_email(email):
        is_valid = True
        if email['email'] is None:
            is_valid = False
            flash("you must enter an address!")
        elif not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        for i in Email.get_all_email():
            if i.email == email['email']:
                flash("Email address is already in use in the system. Please use a different email.")
                is_valid = False
        if is_valid == True:
            flash("Succes! Your email was store in the database.")
        return is_valid
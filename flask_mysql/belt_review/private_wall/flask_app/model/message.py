from flask_app import app 
from flask_app.config.mysqlconnection import MySQLConnection
from flask import session, flash
from flask_app.model import user
db="private_wall_schema"

class Message:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.receiver_id = ['receiver_id']
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.receiver = None
        
    @classmethod
    def create_message(cls, data):
        query = "INSERT INTO messages (user_id, receiver_id, content) VALUES (%(user_id)s, %(receiver_id)s, %(content)s);"
        return MySQLConnection(db).query_db(query, data)

    @classmethod
    def get_messages_by_user_id(cls):
        data = {
            "id" : session["user_id"]
        }
        query = "SELECT * FROM messages WHERE receiver_id = %(id)s;"  
        messages = []      #empty list to append messages to.
        message_data = MySQLConnection(db).query_db(query, data)  #this gets all messages that the logged inuser received
        print(f"this is my message data {message_data}")
        if len(message_data) < 1:
            return False
        for i in message_data:
            this_message = cls(i)  # class instantiation of a message
            this_message.receiver = user.User.get_logged_in_user(session["user_id"]) # associates the user as an user attribute
            this_message.user = user.User.get_one_user(this_message.user_id)
            print(this_message.receiver)
            print(this_message.user)
            messages.append(this_message)
            print(messages)
        return messages
    
    @classmethod
    def number_of_user_messages(cls):

        return len(cls.get_messages_by_user_id())
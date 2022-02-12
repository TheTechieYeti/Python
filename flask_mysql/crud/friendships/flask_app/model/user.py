from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.model import friendship

class User:
    def __init__(self,data):
        pass
db = "friendships_schema"
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = None
        self.friends_list = None

    @classmethod
    def user_create(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES(%(first_name)s,%(last_name)s);"
        connectToMySQL(db).query_db(query, data)
        return 
    @classmethod
    def friendship_create(cls,data):
        query = "INSERT INTO friendships (user_id, friend_id) VALUES(%(user_id)s, %(friend_id)s);"
        connectToMySQL(db).query_db(query, data)
        return 
    @classmethod
    def get_everything(cls):
        query = "SELECT * FROM users;"
        all_users = []
        for i in connectToMySQL(db).query_db(query):
            all_users.append(cls(i))
        return all_users
    @classmethod
    def get_all_friendships(cls):
        all_users = cls.get_everything()
        query = "SELECT * FROM friendships LEFT JOIN users on friend_id = users.id"
        friends = connectToMySQL(db).query_db(query)
        list_of_users = []
        for one_user in all_users: #iterate through user objects
            for friend in friends:      #iterate through dictionary from query
                data = {                    #the information I want from the table
                    'id': friend['friend_id'],    
                    'first_name': friend['first_name'],
                    'last_name': friend['last_name'],
                    'created_at': friend['created_at'],
                    'updated_at': friend['updated_at'],
                    'user_id': friend['user_id']    #this is the id of the user
                }
                if one_user.id == data['user_id']: #this checks to make sure that the user actually has friendships in the friendhips table
                    if one_user.friends_list == None:   #this checks to see if our user object has an empty attribute
                        one_user.friends_list = []      #if it does have and empty attribute, we want to change it to an empty list so we can populate it
                    one_user.friends_list.append(cls(data)) #this creates a user class with the friend information and associates it to our user
            list_of_users.append(one_user)
        return list_of_users  
            
            

        
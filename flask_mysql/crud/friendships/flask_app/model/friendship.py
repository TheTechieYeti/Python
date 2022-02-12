from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model import user
db = "friendships_schema"
class Friendship:
    def __init__(self,data):
        self.user_id = data["user_id"]
        self.friend_id = data["friend_id"]
        self.id = data["id"]
        self.user = None
        self.friend = None

    @classmethod
    def get_all_friendships(cls):
        query = "SELECT * FROM friendships;"
        friendships = connectToMySQL(db).query_db(query)
        
        all_friendships = []
        all_users = user.User.get_everything()
        for i in friendships:
            data = {                  #Isn't this redundant? Our query has only the information we need to created a cls instance
                "user_id":i["user_id"],
                "friend_id":i["friend_id"],
                "id":i["id"]
            }
            one_friendship = cls(data)
            print(f'This is one _friendship object {one_friendship} {one_friendship.user_id}')
            for x in all_users:
                a_user = x
                print(f'this is a test of a_user.id {a_user.id}')
                print(f' comparison test if {a_user.id} == {one_friendship.user_id}')
                if a_user.id == one_friendship.user_id:
                    one_friendship.user = a_user
                if a_user.id == one_friendship.friend_id:
                    one_friendship.friend = a_user
            all_friendships.append(one_friendship)
        print(f'this is my list of friendships {all_friendships}')
        print(f'this is my first friendship user and friend {all_friendships[0].user}, {all_friendships[0].friend}')
        return all_friendships
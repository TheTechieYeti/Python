# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)  #this is not executing properly. Its returning as false and causing an error in my index.html because I can't iterate through a boolean. 
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users where id = %(id)s ;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query, data)  ##We connect first to the function, they query the database using the variable query, and our data which contains our corresponding ID for the user we want. Results is a LIST of dictionarys
        print(f"RESULTS: {results}")
        print(type(results[0]))
        this_user = cls(results[0]) #Here is where we create an instance of user class with the list "results" which contains a dictionary of all the keys and values we need and store it in a variable
        print(this_user)
        print(type(this_user))
        return this_user #We return the variable that stores the instance of the user class we created so when we call that function elsewhere, we get that instance. 

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES( %(fname)s, %(lname)s, %(email)s, NOW(), NOW() );"
        print("user information stored")
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def update(cls, data):  ####### Can't get this to work with updated_at = Now()
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s  WHERE id = %(id)s ;"
        print("user information updated")
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delete(cls, data):
        query = "DELETE from users WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)

    def fullname(self,):
        fullname = f"{self.first_name} {self.last_name}"
        return fullname
            
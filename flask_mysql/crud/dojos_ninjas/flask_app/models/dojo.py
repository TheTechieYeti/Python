from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.students = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results= connectToMySQL('dojos_and_ninjas_schema').query_db(query)  #list of dictionaries. Each dictionary is a row from the database
        alldojos = []
        for i in results:
            alldojos.append(cls(i))
        return alldojos #list of objects

    @classmethod
    def get_one_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data) # a list with a dictionary
        this_dojo = cls(results[0]) #make an object from dictionary
        return this_dojo
    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name, updated_at) VALUES(%(name)s, NOW()); "
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)# a list with a dictionary
        print(f'This is my query {results}')
        dojo = cls( results[0]) #This is making a single dojo object. Because dojo was the default table and we added ninjas to it, the dojo values are default when the class concstructor goes though the data. It only looks for the information it needs. All other duplicate data is titled for the table it was in. 
        print(f'This is my dojo{dojo}')
        for row_in_db in results:
            ninja_data = {
                "id": row_in_db['ninjas.id'],
                "first_name": row_in_db['first_name'],
                "last_name": row_in_db['last_name'],
                "age": row_in_db['age'],
                "created_at": row_in_db['ninjas.created_at'],
                "updated_at": row_in_db['ninjas.updated_at']
            }
            dojo.students.append(ninja.Ninja(ninja_data)) ##This populates the list, that is an attribute of our specific object, with objects corresponding to each student that is in the database. 
        return dojo
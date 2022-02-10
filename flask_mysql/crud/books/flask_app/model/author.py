from mimetypes import init
from msilib.schema import Directory
from flask_app.config.mysqlconnection import connectToMySQL


db='books_schem'
class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']
        self.favorite_books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        list_of_dict_authors = connectToMySQL(db).query_db(query)
        all_authors = []
        for dict in list_of_dict_authors:
            print(dict)
            single_author = cls(dict)
            all_authors.append(single_author)
        
        return all_authors
    @classmethod
    def get_one(cls,data):
        query = "Select * FROM authors WHERE id = %(id)s;"
        list_with_dict = connectToMySQL(db).query_db(query, data)
        one_author = cls(list_with_dict[0])

        return one_author 
    @classmethod
    def author_create(cls, data):
        query = "INSERT INTO authors (name) VALUES(%(name)s);"
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def author_favorite_create(cls,data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES(%(author_id)s,%(book_id)s);"
        connectToMySQL(db).query_db(query,data)
        return 
    @classmethod
    def get_author_favorites(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = author_id LEFT JOIN books ON book_id = books.id WHERE authors.id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
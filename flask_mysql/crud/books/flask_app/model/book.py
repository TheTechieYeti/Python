from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.model import author

db='books_schem'
class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_authors = []

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books"
        results = MySQLConnection(db).query_db(query)
        all_books = []
        for i in results:
            all_books.append(cls(i))
        return all_books
    
    @classmethod
    def get_book(cls, data):
        bookquery='SELECT * FROM books where id = %(id)s'
        return MySQLConnection(db).query_db(bookquery, data)    
     
    @classmethod
    def book_create(cls, data):
        query = "INSERT INTO books (author_id,title, num_pages) VALUES(4, %(title)s, %(num_pages)s);"
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def book_author_favorite(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        baf_results = connectToMySQL(db).query_db(query,data)
        print(baf_results)
        books_fav_authors = []
        for i in baf_results:
            data = {
                "id": i["authors.id"],
                "name": i["name"],
                "created_at": i["authors.created_at"],
                "update_at": i["update_at"]
            }
            books_fav_authors.append(author.Author(data))
        return books_fav_authors
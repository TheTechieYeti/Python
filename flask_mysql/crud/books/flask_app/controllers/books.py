from flask_app import app
from flask import render_template, redirect, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.model import book, author

db='books_schem'
@app.route('/books')         
def books():
    every_books = book.Book.get_all_books()
    print(every_books)
    return render_template("books.html", books=every_books)

@app.route('/books/<int:id>')         
def single_book(id):
    data = {
        'id':id
    }
    
    uno_book = book.Book(book.Book.get_book(data)[0])
    all_authors = author.Author.get_all()
    uno_book.favorite_authors = book.Book.book_author_favorite(data)
    print(f'These are my books favorite authors{uno_book.favorite_authors}')
    return render_template("onebook.html", book=uno_book, authors=all_authors)

@app.route('/books/create', methods=["POST"])         
def create_book():
    data = {
        "title":request.form['book_title'],
        "num_pages": request.form['book_length']
    }
    book.Book.book_create(data)
    return redirect("/books")

@app.route('/book_author_favorite', methods = ["POST"])         
def book_author_favorite():
    data = {
        "author_id" : request.form['author_id'],
        "book_id" : request.form['book_id']
    }
    author.Author.author_favorite_create(data)
    return redirect(f'/books/{data["book_id"]}')
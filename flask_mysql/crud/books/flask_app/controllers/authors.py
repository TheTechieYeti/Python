from flask_app import app
from flask import render_template, redirect, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.model import author, book
@app.route('/')         
def index():
    return redirect("/authors")

@app.route('/authors')         
def authors():
    all_authors = author.Author.get_all()
    return render_template("authors.html", authors=all_authors)

@app.route('/authors/<int:author_id>')         
def single_author(author_id):
    data = {
        "id": author_id
    }
    single_author = author.Author.get_one(data)
    all_books = book.Book.get_all_books()
    print(f'This is my author{single_author}')
    gaf_results = author.Author.get_author_favorites(data)
    for a_book in gaf_results:
        single_author.favorite_books.append(book.Book(a_book))
    print(f'These are my authors favorite books {single_author.favorite_books}')
    return render_template("oneauthor.html", single_author=single_author, all_books=all_books)

@app.route('/authors/create', methods=["POST"])         
def create():
    data = {
        "name":request.form['author_name']
    }
    author.Author.author_create(data)
    return redirect("/authors")

@app.route('/author_favorite_book', methods=["POST"])         
def author_favorite_book():
    data = {
        "author_id": request.form['author_id'],
        "book_id": request.form['book_id'],
    }
    author_id = data["author_id"]
    print(author_id)
    author.Author.author_favorite_create(data)
    return redirect(f'/authors/{author_id}')
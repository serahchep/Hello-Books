from flask import Flask
from flask import Flask, request, jsonify
from flask import Blueprint
from models import Books
from books import book

book = Blueprint('book', __name__)
APP = Flask(__name__)
APP.config["TESTING"] = True

MY_BOOK = Books()
Books= {}

sent_data = request.get_json(force=True)
#endpoint to add book and get all books
methods=['GET', 'POST']
def books():
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        edition = data.get('edition')
        book_id = data.get('book_id')
        response = jsonify(title, author, edition, book_id)
        response.status_code = 200

        return response

    #get all books method="GET"
    get_books = MY_BOOK.get_all()
    response = jsonify(get_books)
    response.status_code = 200

    return response
# endpoint to edit, modify and delete a book by id
@APP.route('/api/v1/books/<int:book_id>', methods=['PUT', 'GET', 'DELETE'])
#get a book by its id
def book_book_id(book_id):
    if request.method == 'GET':
        get_book = MY_BOOK.get_single_book(book_id)
        response = jsonify(get_book)
        response.status_code = 200

        return response
 #mupdate a book method
    elif request.method == 'PUT':
   
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        edition = data.get('edition')
        response = jsonify(MY_BOOK.edit_book(title, author, edition, book_id))
        response.status_code = 200

        return response

    
    #method=DELETE
    response = jsonify(MY_BOOK.delete(book_id))
    

    return response

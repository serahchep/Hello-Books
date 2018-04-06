from flask import Blueprint
from flask_restful import Api

from .views import Booksurl, Bookurl

book_BP = Blueprint('book', __name__)
api = Api(book_BP)

api.add_resource(Booksurl, '/api/v1/books/')
api.add_resource(Bookurl, '/api/v1/books/<book_id>')


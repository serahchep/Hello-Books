from flask import Flask
from flask import Flask, jsonify, abort


all_books = {}


class Books(object):
   
    def __init__(self, title, author, edition, book_id):
        self.title= title
        self.author = author
        self.edition = edition
        self.book_id = book_id


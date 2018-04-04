from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash

all_books = []

class Books():
   
    def __init__(self):
        self.book = {}

    def get_all(self):
        
        return all_books

    def get_single_book(self, book_id):
      
        if book_id in all_books:
            return all_books[book_id]

        return {"message":"Book not found"}

    def put(self, title, author, edition, book_id):
       
        if book_id in all_books:
            return {"message":"Book id entered already exists"}

        self.book["title"] = title
        self.book["author"] = author
        self.book["edition"] = edition

        all_books[book_id] = self.book
        return all_books[book_id]

    #edit a book by its id
    def edit_book(self, title, author, edition, book_id):
        if book_id in all_books:
            self.book["title"] = title
            self.book["author"] = author
            self.book["edition"] = edition

            all_books[book_id] = self.book
            return all_books[book_id]
        return {"message":"Book you are trying to edit doesn't exist"}

    def delete(self, book_id):
        
        if book_id in all_books:
            del all_books[book_id]
            return {"message":"Book {} deleted successfully".format(book_id)}
       
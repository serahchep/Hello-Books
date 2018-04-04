from flask import Flask
import random
import string
from werkzeug.security import generate_password_hash, check_password_hash
# from books import models
USERS = {}

all_books={}
class Users():
    #class to represent users model

    def __init__(self):
        self.user = {}
 #add a user to USERS
    def put(self,username, email, password):
        if username in USERS:
            return {"message": "Username already exists"}
        self.user["email"] = email
        pw_hash = generate_password_hash(password)
        self.user["password"] = pw_hash
        USERS[username] = self.user
        return {username: USERS[username]}

 #verify password
    
    def verify_password(self, username, password):
        if username in USERS:
            result = check_password_hash(USERS[username]["password"], password)
        if result is True:
            return "True"
        return {"message": "Password incorrect"}
        return {"message": "Incorrect username"}

#borrow a book by book_id
    def borrow_book(self, book_id):
        if book_id in all_books:
            return {"message": "Book successfully checked out"}
            return {"message": "Book not found"}

#reset user password
    def reset_password(self, username):
        if username in USERS:
            new_password = ''.join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        pw_hash = generate_password_hash(new_password)
        USERS[username]["password"] = pw_hash

        return {"new password": new_password}
        return {"message": "Incorrect username"}

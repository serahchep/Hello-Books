from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["TESTING"] = True

# check if jwt token is in blacklist
app.config['JWT_SECRET_KEY'] = 'my-key'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)

from .books import book_BP as book_BluePrint
app.register_blueprint(book_BluePrint)

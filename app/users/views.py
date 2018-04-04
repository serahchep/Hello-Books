from flask import Flask, request, jsonify
from flask import Blueprint
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, get_jti,
     jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt
 )
from models import Users


#user = Blueprint('user', __name__)
APP = Flask(__name__)
APP.config["TESTING"] = True

#check if jwt token is in blacklist
APP.config['JWT_SECRET_KEY'] = 'my-key'
APP.config['JWT_BLACKLIST_ENABLED'] = True
APP.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(APP)

BLACKLIST = set()
jwt.token_in_blacklist_loader
def check_if_token_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in BLACKLIST
USERS = {}
MY_USER = Users()

@APP.route('/api/v1/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if len(password) < 4:
        return jsonify({"message": "password is too short"})
    if confirm_password != password:
        return jsonify({"message": "Passwords don't match"})
        response = jsonify(MY_USER.put(username, email, password))
    response.status_code = 200
    return response


@APP.route('/api/v1/users/books/<int:book_id>', methods=['POST'])
@jwt_required
def users_books(book_id):
    response = jsonify(MY_USER.borrow_book(book_id))
    response.status_code = 200
    return response


@APP.route('/api/v1/auth/login', methods=['POST'])
def login():
    #login user by verifying password and creating an access token'''
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    auth = MY_USER.verify_password(username, password)

    if auth == "True":
        access_token = create_access_token(identity=username)
        return access_token

    response = jsonify(auth)
    response.status_code = 401
    return response


@APP.route('/api/v1/auth/logout', methods=['POST'])
@jwt_required
def logout():
    '''logout user by revoking password'''
    jti = get_raw_jwt()['jti']
    BLACKLIST.add(jti)
    return jsonify({"message": "Successfully logged out"})

#reset user password'''
@APP.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    
    data = request.get_json()
    username = data.get("username")

    response = jsonify(MY_USER.reset_password(username))
    response.status_code = 200
    return response


#method to run app.py
if __name__ == '__main__':
 APP.run(debug=True)
from flask import Flask, jsonify
from app import app
from models import Users
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, get_jti,
    jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt
)
from .models import Users

# check if jwt token is in blacklist
app.config['JWT_SECRET_KEY'] = 'my-key'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)

BLACKLIST = set()
jwt.token_in_blacklist_loader


def check_if_token_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in BLACKLIST


USERS = {}

MY_USER = Users()


class RegisterResource(Resource):
    user_parser = reqparse.RequestParser()
    user_parser.add_argument('username')
    user_parser.add_argument('email')
    user_parser.add_argument('password')

    @jwt_required
    def post(self):
        user_args = self.user_parser.parse_args()
        confirm_password = user_args['confirm_password']
        username = user_args['username']
        email = user_args['email']
        password = user_args['password']

        if len(password) < 4:
             response = jsonify({"message": "password is too short"})
        if confirm_password != password:

            response = jsonify({"message": "Passwords don't match"})
            response = jsonify(USERS.put(username, email, password))
        response.status_code = 200
        return response


#@APP.route('/api/v1/users/books/<int:book_id>', methods=['POST'])
#@jwt_required
#def post(self):
   # response = jsonify(MY_USER.borrow_book(book_id))
    #response.status_code = 200
   # return response


class LoginResource(Resource):

    login_parser = reqparse.RequestParser()

    @jwt_required
    def post(self):

        # login user by verifying password and creating an access token'''

        login_args = self.login_parser.parse_args()
        username = login_args['email']
        password = login_args['password']
        self.login_parser = reqparse.RequestParser()
        if username != 'test' or password != 'test':
            return jsonify({"msg": "Bad username or password"}), 401

        ret = {'access_token': create_access_token(username)}
        return jsonify(ret), 200

        auth = MY_USER.verify_password(username, password)

        if auth == "True":
            access_token = create_access_token(identity=username)
            return access_token

        response = jsonify(auth)
        response.status_code = 401
        return response


class LogoutResource(Resource):
    @jwt_required
    def post(self):
        '''logout user by revoking password'''

    jti = get_raw_jwt()['jti']
    BLACKLIST.add(jti)
    response = jsonify({"message": "Successfully logged out"})


# reset user password'''
class ResetPasswordResource(Resource):
    reset_pass_parser = reqparse.RequestParser()

    def post(self):
        reset_pass_args = self.reset_pass_parser.parse_args()
        username = reset_pass_args['username']
        user_token = reset_pass_args['reset_token']
        response = jsonify(MY_USER.reset_password(username))
        response.status_code = 200
        return response

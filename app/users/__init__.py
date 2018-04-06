from flask import Blueprint
from flask_restful import Api

from .views import Resource
user_BP = Blueprint('user', __name__)
api = Api(user_BP)
from .views import RegisterResource, LoginResource, \
    LogoutResource, ResetPasswordResource

api.add_resource(Resource, '/api/v1/auth')
api.add_resource(RegisterResource, '/register', endpoint="register")

api.add_resource(LoginResource, '/login', endpoint="login")

api.add_resource(LogoutResource, '/logout', endpoint='logout')

api.add_resource(ResetPasswordResource, '/reset-password',
                 endpoint='reset-password')


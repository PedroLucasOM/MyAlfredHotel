from flask import make_response, render_template
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from flask_restful import Resource, reqparse
from werkzeug.exceptions import NotFound, BadRequest
from werkzeug.security import safe_str_cmp

from blacklist import BLACKLIST
from model.user import UserModel
from utils.utils import non_empty_string

arguments = reqparse.RequestParser(bundle_errors=True)
arguments.add_argument('fullname', required=True, nullable=False, type=non_empty_string,
                       help='The field Fullname cannot be left blank')
arguments.add_argument('email', required=True, nullable=False, type=non_empty_string,
                       help='The field E-mail cannot be left blank')
arguments.add_argument('login', required=True, nullable=False, type=non_empty_string,
                       help='The field Login cannot be left blank')
arguments.add_argument('password', type=non_empty_string, required=True, nullable=False,
                       help='The field Password cannot be left blank')
arguments.add_argument('activated', type=bool)


class UserConfirm(Resource):
    @classmethod
    def get(cls, id):
        user = UserModel.findExists(id)
        user.activated = True
        user.save()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('user_confirmed.html'), 200, headers)


class UserLoginResource(Resource):
    def post(self):
        arguments_copy = arguments
        arguments_copy.remove_argument('fullname')
        arguments_copy.remove_argument('email')
        data = arguments_copy.parse_args()
        user = UserModel.findByLogin(data['login'])
        if user and safe_str_cmp(user.password, data['password']):
            if user.activated:
                access_token = create_access_token(identity=user.id)
                return {'access_token': access_token}, 200
            return BadRequest('User not confirmed.')
        return {'message': 'The username or password is incorrect.'}, 401


class UserLogoutResource(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {}, 204


class UserResourceAll(Resource):
    @jwt_required
    def get(self):
        return [user.json() for user in UserModel.query.all()]

    def post(self):
        data = arguments.parse_args()
        if UserModel.findByLogin(data['login']):
            return BadRequest('The informed login already exists.')
        if UserModel.findByEmail(data['email']):
            return BadRequest('The informed email already exists.')
        user = UserModel(**data)
        user.activated = False
        user.save()
        user.send_confirmation_email()
        return user.json(), 201


class UserResource(Resource):
    @jwt_required
    def get(self, id):
        user = UserModel.findById(id)
        if user:
            return user.json()
        raise NotFound('User not found')

    @jwt_required
    def put(self, id):
        saved_user = UserModel.findExists(id)
        data = arguments.parse_args()
        saved_user.update(**data)
        saved_user.save()
        return saved_user.json(), 200

    @jwt_required
    def delete(self, id):
        user = UserModel.findExists(id)
        user.delete()
        return {}, 204

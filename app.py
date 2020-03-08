from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from blacklist import BLACKLIST
from resource.hotel import HotelResource, HotelResourceAll
from resource.user import UserResource, UserResourceAll, UserLoginResource, UserLogoutResource
from sql_alchemy import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'MyAlfredHotel'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
database.init_app(app)
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    database.create_all()


@jwt.token_in_blacklist_loader
def verify_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def invalid_token():
    return jsonify({'message': 'You have been logged out'}), 401


api.add_resource(HotelResourceAll, '/hotels')
api.add_resource(HotelResource, '/hotels/<int:id>')
api.add_resource(UserResourceAll, '/users')
api.add_resource(UserResource, '/users/<int:id>')
api.add_resource(UserLoginResource, '/login')
api.add_resource(UserLogoutResource, '/logout')

if __name__ == '__main__':
    app.run(debug=True)

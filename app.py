from flask import Flask
from flask_restful import Api

from resource.hotel import HotelResource, HotelResourceAll
from sql_alchemy import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)
api = Api(app)


@app.before_first_request
def create_tables():
    database.create_all()


api.add_resource(HotelResourceAll, '/hotels')
api.add_resource(HotelResource, '/hotels', '/hotels/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)

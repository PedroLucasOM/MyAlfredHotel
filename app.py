from flask import Flask
from flask_restful import Api
from resource.hotel import HotelResource, HoteisResource

app = Flask(__name__)
api = Api(app)

api.add_resource(HoteisResource, '/hoteis')
api.add_resource(HotelResource, '/hoteis/<string:id>')

if(__name__ == '__main__' ):
    app.run(debug=True)

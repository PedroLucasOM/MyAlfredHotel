from flask_restful import Resource, reqparse
from werkzeug.exceptions import NotFound

from model.hotel import HotelModel


def addArgs(arguments):
    arguments.add_argument('id')
    arguments.add_argument('name')
    arguments.add_argument('classification')
    arguments.add_argument('cep')
    arguments.add_argument('address')
    arguments.add_argument('neighborhood')
    arguments.add_argument('city')
    arguments.add_argument('state')


class HotelResourceAll(Resource):
    arguments = reqparse.RequestParser()
    addArgs(arguments)

    def get(self):
        return [hotel.json() for hotel in HotelModel.query.all()]

    def post(self):
        arguments = reqparse.RequestParser()
        addArgs(arguments)

        data = HotelResource.arguments.parse_args()
        hotel = HotelModel(**data)
        hotel.save()
        return hotel.json(), 201


class HotelResource(Resource):
    arguments = reqparse.RequestParser()
    addArgs(arguments)

    def get(self, id):
        hotel = HotelModel.find(id)
        if hotel:
            return hotel.json()
        raise NotFound('Hotel not found')

    def put(self, id):
        saved_hotel = HotelModel.findExists(id)
        data = HotelResource.arguments.parse_args()
        saved_hotel.update(**data)
        saved_hotel.save()
        return saved_hotel.json(), 200

    def delete(self, id):
        hotel = HotelModel.findExists(id)
        hotel.delete()
        return 204

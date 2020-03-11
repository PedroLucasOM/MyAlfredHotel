from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from werkzeug.exceptions import NotFound

from model.hotel import HotelModel
from utils.utils import non_empty_string

arguments = reqparse.RequestParser(bundle_errors=True)
arguments.add_argument('name', type=non_empty_string, required=True, nullable=False,
                       help='The field Name cannot be left blank')
arguments.add_argument('classification', required=True, nullable=False, type=float,
                       help='The field Classification cannot be null')
arguments.add_argument('cep', type=non_empty_string, required=True, nullable=False,
                       help='The field CEP cannot be null')
arguments.add_argument('address', type=non_empty_string, required=True, nullable=False,
                       help='The field Address cannot be left blank')
arguments.add_argument('neighborhood', type=non_empty_string, required=True, nullable=False,
                       help='The field Neighborhood cannot be left blank')
arguments.add_argument('city', type=non_empty_string, required=True, nullable=False,
                       help='The field City cannot be left blank')
arguments.add_argument('state', type=non_empty_string, required=True, nullable=False,
                       help='The field State cannot be left blank')
arguments.add_argument('id_site', type=int, required=True, nullable=False,
                       help="Every hotel needs to be linked with a site.")


class HotelResourceAll(Resource):
    @jwt_required
    def get(self):
        return [hotel.json() for hotel in HotelModel.query.all()]

    @jwt_required
    def post(self):
        data = arguments.parse_args()
        hotel = HotelModel(**data)
        hotel.save()
        return hotel.json(), 201


class HotelResource(Resource):
    @jwt_required
    def get(self, id):
        hotel = HotelModel.findById(id)
        if hotel:
            return hotel.json()
        raise NotFound('Hotel not found')

    @jwt_required
    def put(self, id):
        saved_hotel = HotelModel.findExists(id)
        data = arguments.parse_args()
        saved_hotel.update(**data)
        saved_hotel.save()
        return saved_hotel.json(), 200

    @jwt_required
    def delete(self, id):
        hotel = HotelModel.findExists(id)
        hotel.delete()
        return {}, 204

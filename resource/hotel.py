from flask_restful import Resource, reqparse
from model.hotel import HotelModel

hoteis = []

class HoteisResource(Resource):
    def get(self):
        return hoteis

class HotelResource(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('classificacao')
    argumentos.add_argument('cep')
    argumentos.add_argument('logradouro')
    argumentos.add_argument('bairro')
    argumentos.add_argument('cidade')
    argumentos.add_argument('estado')

    def find_hotel(id):
        for hotel in hoteis:
            if(hotel['id'] == id):
                return hotel
        return None

    def get(self, id):
        hotel = HotelResource.find_hotel(id)
        if hotel:
            return hotel
        return {'message' : 'Hotel not found'}, 404


    def post(self, id):
        dados = HotelResource.argumentos.parse_args()
        hotel = HotelModel(id, **dados).json()
        hoteis.append(hotel)
        return hotel, 201

    def put(self, id):
        hotel_salvo = HotelResource.find_hotel(id)
        if hotel_salvo:
            dados = HotelResource.argumentos.parse_args()
            hotel = HotelModel(id, **dados).json()
            hotel_salvo.update(hotel)
            return hotel_salvo, 200
        return {'message': 'Hotel not found'}, 404

    def delete(self, id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['id'] != id]
        return {'message': 'Hotel deleted'}, 204

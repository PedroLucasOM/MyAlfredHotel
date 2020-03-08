from werkzeug.exceptions import BadRequest

from sql_alchemy import database


class HotelModel(database.Model):
    __tablename__ = 'hotels'

    id = database.Column(database.Integer, primary_key=True, nullable=False)
    name = database.Column(database.String(100), nullable=False)
    classification = database.Column(database.Float(precision=1), nullable=False)
    cep = database.Column(database.String(20), nullable=False)
    address = database.Column(database.String(100), nullable=False)
    neighborhood = database.Column(database.String(100), nullable=False)
    city = database.Column(database.String(100), nullable=False)
    state = database.Column(database.String(100), nullable=False)

    def __init__(self, id, name, classification, cep, address, neighborhood, city, state):
        self.id = id
        self.name = name
        self.classification = classification
        self.cep = cep
        self.address = address
        self.neighborhood = neighborhood
        self.city = city
        self.state = state

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'classification': self.classification,
            'cep': self.cep,
            'address': self.address,
            'neighborhood': self.neighborhood,
            'city': self.city,
            'state': self.state
        }

    @classmethod
    def find(cls, id):
        hotel = cls.query.filter_by(id=id).first()
        if hotel:
            return hotel
        return None

    @classmethod
    def findExists(cls, id):
        hotel = HotelModel.find(id)
        if hotel:
            return hotel
        raise BadRequest('The informed hotel does not exist.')

    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, id, name, classification, cep, address, neighborhood, city, state):
        self.name = name
        self.classification = classification
        self.cep = cep
        self.address = address
        self.neighborhood = neighborhood
        self.city = city
        self.state = state

    def delete(self):
        database.session.delete(self)
        database.session.commit()

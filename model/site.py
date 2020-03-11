from werkzeug.exceptions import BadRequest

from sql_alchemy import database


class SiteModel(database.Model):
    __tablename__ = 'sites'

    id = database.Column(database.Integer, primary_key=True)
    url = database.Column(database.String(80))
    hotels = database.relationship('HotelModel')

    def __init__(self, url):
        self.url = url

    def json(self):
        return {
            'id': self.id,
            'url': self.url,
            'hotels': [hotel.json() for hotel in self.hotels]
        }

    @classmethod
    def findById(cls, id):
        site = cls.query.filter_by(id=id).first()
        if site:
            return site
        return None

    @classmethod
    def findExists(cls, id):
        site = SiteModel.findById(id)
        if site:
            return site
        raise BadRequest('The informed site does not exist.')

    def save(self):
        database.session.add(self)
        database.session.commit()

    def delete(self):
        [hotel.delete() for hotel in self.hotels]
        database.session.delete(self)
        database.session.commit()

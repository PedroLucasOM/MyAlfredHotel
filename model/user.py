from werkzeug.exceptions import BadRequest

from sql_alchemy import database


class UserModel(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True, nullable=False)
    fullname = database.Column(database.String(100), nullable=False)
    login = database.Column(database.String(100), nullable=False, unique=True)
    password = database.Column(database.String(100), nullable=False)

    def __init__(self, fullname, login, password):
        self.fullname = fullname
        self.login = login
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'login': self.login
        }

    @classmethod
    def findById(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None

    @classmethod
    def findByLogin(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    @classmethod
    def findExists(cls, id):
        user = UserModel.findById(id)
        if user:
            return user
        raise BadRequest('The informed user does not exist.')

    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, fullname, login, password):
        self.fullname = fullname
        self.login = login
        self.password = password

    def delete(self):
        database.session.delete(self)
        database.session.commit()

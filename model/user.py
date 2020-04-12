from flask import request, url_for, render_template
from requests import post
from werkzeug.exceptions import BadRequest

from sql_alchemy import database

MAILGUN_DOMAIN = 'sandboxcfabe88e830f415086a882d0c8b1ed6f.mailgun.org'
MAILGUN_API_KEY = '0563b015a7adbe26a8e845376a387d4a-aa4b0867-45f82a37'
FROM_TITLE = 'NO-REPLY'
FROM_EMAIL = 'pedro99lucasom@gmail.com'


class UserModel(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True, nullable=False)
    fullname = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(100), nullable=False, unique=True)
    login = database.Column(database.String(100), nullable=False, unique=True)
    password = database.Column(database.String(100), nullable=False)
    activated = database.Column(database.Boolean, default=False)

    def __init__(self, fullname, email, login, password, activated):
        self.fullname = fullname
        self.email = email
        self.login = login
        self.password = password
        self.activated = activated

    def json(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'email': self.email,
            'login': self.login,
            'activated': self.activated
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
    def findByEmail(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None

    @classmethod
    def findExists(cls, id):
        user = UserModel.findById(id)
        if user:
            return user
        raise BadRequest('The informed user does not exist.')

    def send_confirmation_email(self):
        registration_link = request.url_root[:-1] + url_for('userconfirm', id=self.id)
        post('https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN),
             auth=('api', MAILGUN_API_KEY),
             data={'from': '{} <{}>'.format(FROM_TITLE, FROM_EMAIL),
                   'to': self.email,
                   'subject': 'Confirmação de Cadastro',
                   'text': 'Confirme seu cadastro clicando no link a seguir: {}'.format(registration_link),
                   'html': render_template('user_confirm.html', registration_link=registration_link)
                   }
             )

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

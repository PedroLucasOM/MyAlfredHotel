from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from werkzeug.exceptions import NotFound, BadRequest

from model.site import SiteModel
from utils.utils import non_empty_string

arguments = reqparse.RequestParser(bundle_errors=True)
arguments.add_argument('url', type=non_empty_string, required=True, nullable=False,
                       help='The field URL cannot be left blank')


class SiteResourceAll(Resource):
    @jwt_required
    def get(self):
        return [site.json() for site in SiteModel.query.all()]

    @jwt_required
    def post(self):
        data = arguments.parse_args()
        if SiteModel.findExists(data['url']):
            raise BadRequest('The informed URL already exists.')
        site = SiteModel(**data)
        site.save()
        return site.json(), 201


class SiteResource(Resource):
    @jwt_required
    def get(self, id):
        site = SiteModel.findById(id)
        if site:
            return site.json()
        raise NotFound('Site not found')

    @jwt_required
    def delete(self, id):
        site = SiteModel.findExists(id)
        site.delete()
        return {}, 204

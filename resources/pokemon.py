from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api.schemas import PokemonSchema
from api.services import PokemonServices


class PokemonResource(Resource):
    schema = PokemonSchema()
    service = PokemonServices

    def get(self):
        if not request.args.to_dict():
            response = self.service.get_all()
            return self.schema.dump(response, many=True)

        params = request.args.to_dict()
        response = self.service.get_filters(**params)
        return self.schema.dump(response, many=True)

    @jwt_required()
    def post(self):
        pass

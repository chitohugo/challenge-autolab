from flask_jwt_extended import jwt_required
from flask_restful import Resource


class PokemonResource(Resource):
    @jwt_required()
    def get(self):
        return "Hello!"

    def post(self):
        pass

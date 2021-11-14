from flasgger import swag_from
from flask import request, current_app
from flask_jwt_extended import jwt_required
from flask_restful import Resource, Api

from api.schemas import PokemonSchema
from api.services import PokemonServices

app = current_app


class PokemonResource(Resource):
    schema = PokemonSchema()
    service = PokemonServices

    @jwt_required()
    @swag_from('swagger/pokemon.yml')
    def get(self):
        api = Api(app)

        params = request.args.to_dict()

        if "filters" not in params and "sort" not in params:
            page = int(params.get("page")) if "page" in params else None
            per_page = int(params.get("limit")) if "limit" in params else None
            response = self.service.get_all(page, per_page)
            next_url, prev_url = next_prev_url(api, response)

            return {
                "data":
                    self.schema.dump(response.items, many=True),
                "next": next_url,
                "prev": prev_url
            }

        response = self.service.get_filters(**params)
        next_url, prev_url = next_prev_url(api, response)

        return {
            "data":
                self.schema.dump(response.items, many=True),
            "next": next_url,
            "prev": prev_url
        }


def next_prev_url(api, pages):
    next_url = api.url_for(PokemonResource,
                           page=pages.next_num) if pages.has_next else None
    prev_url = api.url_for(PokemonResource,
                           page=pages.prev_num) if pages.has_prev else None
    return next_url, prev_url

from flask_marshmallow import Marshmallow

from api.model import Pokemon

ma = Marshmallow()


class PokemonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemon
        ordered = True

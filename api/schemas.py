from flask_marshmallow import Marshmallow, fields
from marshmallow import pre_load
from werkzeug.security import generate_password_hash

from api.model import Pokemon

ma = Marshmallow()


class PokemonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemon
        ordered = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True

    id = fields.fields.Integer(dump_only=True)
    username = fields.fields.String(required=True)
    email = fields.fields.Email(required=True)
    password = fields.fields.Method(
        required=True, deserialize="load_password"
    )

    created_at = fields.fields.DateTime(dump_only=True)
    updated_at = fields.fields.DateTime(dump_only=True)

    @staticmethod
    def load_password(value):
        return generate_password_hash(value)

    # Clean up data
    @pre_load
    def process_input(self, data, **kwargs):
        data["email"] = data["email"].lower().strip()
        return data


class LoginSchema(ma.SQLAlchemyAutoSchema):
    email = fields.fields.Email(required=True)
    password = fields.fields.String(required=True)
    access_token = fields.fields.String(dump_only=True)
    user_id = fields.fields.String(dump_only=True)

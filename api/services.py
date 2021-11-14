import json

from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from api.model import Pokemon, User


class PokemonServices:
    @classmethod
    def get_all(cls, page, limit):
        result = Pokemon.get_all(page, limit)
        return result

    @classmethod
    def get_filters(cls, **params):
        filter_fields = {}
        _order_by = Pokemon.id.asc
        if "filters" in params:
            filter_fields = json.loads(params.get("filters"))
        if "sort" in params:
            sort_field = params.get("sort")
            sort = sort_field.split(":")
            field = sort[0]
            direction = sort[1]
            _order = getattr(Pokemon, field)
            _order_by = getattr(_order, direction)
        page = int(params.get("page")) if "page" in params else None
        per_page = int(params.get("limit")) if "limit" in params else None
        result = Pokemon.get_filters(filter_fields, _order_by, page, per_page)
        return result


class SignupServices:
    @classmethod
    def validate_register(cls, data):
        """Validate if user and email."""

        if User.get_by_username(data["username"]):
            return {
                "message":
                    f"Username {data['username']} already exist"
            }

        if User.get_by_email(data["email"]):
            return {
                "message":
                    "Email {data['username']} already exist {data['email']}"
            }

        user = User(**data)
        user.save()
        return user


class LoginServices:
    @classmethod
    def validate_login(cls, data):
        user = User.get_by_email(data['email'])

        if not user or not check_password_hash(user.password, data['password']):
            return "username or password is incorrect"

        access_token = create_access_token(identity=user.id, fresh=True)

        if user and check_password_hash(user.password, data['password']):
            return {
                        "user_id": user.id,
                        "email": user.email,
                        "access_token": access_token
                    }
        return "Unable to authenticate user: Invalid credentials"


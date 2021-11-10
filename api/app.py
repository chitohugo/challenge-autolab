from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from werkzeug import exceptions

from api.config import env_config
from api.model import db
from resources.pokemon import PokemonResource
from utils import errors

api = Api()
jwt = JWTManager()


def create_app(config_name):
    import resources

    app = Flask(__name__)

    app.config.from_object(env_config[config_name])
    db.init_app(app)
    Migrate(app, db)
    api.init_app(app)
    jwt.init_app(app)

    app.register_error_handler(exceptions.NotFound, errors.handle_404_errors)

    app.register_error_handler(
        exceptions.InternalServerError, errors.handle_server_errors
    )

    app.register_error_handler(exceptions.BadRequest, errors.handle_400_errors)

    app.register_error_handler(FileNotFoundError, errors.handle_400_errors)

    app.register_error_handler(TypeError, errors.handle_400_errors)

    app.register_error_handler(KeyError, errors.handle_404_errors)

    app.register_error_handler(AttributeError, errors.handle_400_errors)

    app.register_error_handler(ValueError, errors.handle_400_errors)

    app.register_error_handler(AssertionError, errors.handle_400_errors)

    return app


api.add_resource(PokemonResource, "/pokemon", endpoint="pokemon")

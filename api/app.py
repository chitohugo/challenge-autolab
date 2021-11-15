from flasgger import Swagger
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from api.config import env_config
from api.model import db
from api.schemas import ma
from resources.login import LoginResource
from resources.pokemon import PokemonResource
from resources.signup import SignupResource

api = Api()
jwt = JWTManager()
swagger = Swagger()


def create_app(config_name):
    import resources

    app = Flask(__name__)

    app.config.from_object(env_config[config_name])
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    api.init_app(app)
    jwt.init_app(app)
    template = {
        "swagger": "2.0",
        "info": {
            "title": "AutoLab Challenge",
            "description": "Flask-Restful",
            "version": "0.1.1",
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
            }
        },
        "security": [
            {
                "Bearer": []
            }
        ]

    }
    app.config['SWAGGER'] = {
        'title': 'APIs Challenge Pokemon',
        'uiversion': 3,
    }

    Swagger(app, template=template)

    return app


api.add_resource(PokemonResource,
                 "/v1/api/pokemon",
                 endpoint="pokemon"
                 )
api.add_resource(SignupResource,
                 "/v1/api/signup",
                 endpoint="signup"
                 )
api.add_resource(LoginResource,
                 "/v1/api/login",
                 endpoint="login"
                 )

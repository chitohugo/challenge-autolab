from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from api.schemas import LoginSchema
from api.services import LoginServices


class LoginResource(Resource):
    service = LoginServices
    schema = LoginSchema()

    @swag_from('swagger/login.yml', validation=True)
    def post(self):
        """login in existing user."""

        try:
            payload = request.get_json()
            data = self.schema.load(payload)
            response = self.service.validate_login(data)
            if isinstance(response, dict):
                data = self.schema.dump(response)
                return data, HTTPStatus.OK

            return response, HTTPStatus.UNAUTHORIZED
        except ValidationError as err:
            return {"errors": err.messages}, HTTPStatus.FAILED_DEPENDENCY

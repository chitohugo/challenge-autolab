from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from api.model import User
from api.schemas import UserSchema
from api.services import SignupServices


class SignupResource(Resource):
    service = SignupServices
    schema = UserSchema()

    @swag_from('swagger/signup.yml', validation=True)
    def post(self):
        """Create new user.

        Args:
        payload: dictionary with email, username and password fields

        Returns:
            A user created.
        """
        try:
            payload = request.get_json()
            data = self.schema.load(payload)
            response = self.service.validate_register(data)
            if isinstance(response, User):
                data = self.schema.dump(response)
                return data, HTTPStatus.CREATED

            return response, HTTPStatus.BAD_REQUEST

        except ValidationError as err:
            return {"errors": err.messages}, HTTPStatus.FAILED_DEPENDENCY


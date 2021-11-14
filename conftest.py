import json

import pytest

from api.app import create_app
from api.model import User, Pokemon, db


@pytest.fixture()
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture()
def create_user():
    payload = {
        "email": "testing@gmail.com",
        "username": "test@test",
        "password": "testing#test"
    }
    user = User(**payload)
    return user


@pytest.fixture()
def create_pokemon():
    payload = {
        "name": "Bulbasaur",
        "type_1": "Grass",
        "type_2": "Poison",
        "total": 318,
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "sp_atk": 65,
        "sp_def": 65,
        "speed": 45,
        "generation": 1,
        "legendary": False
    }
    pokemon = Pokemon(**payload)
    return pokemon


@pytest.fixture()
def register(client):
    response = client.post(
        '/v1/api/signup',
        data=json.dumps(dict(
            username='test',
            email='testing@realpython.com',
            password='testing'
        )),
        content_type='application/json',
    )
    return response


@pytest.fixture()
def login(client, create_user):
    response = client.post(
        '/v1/api/login',
        data=json.dumps(dict(
            email='testing@realpython.com',
            password='testing'
        )),
        content_type='application/json',
    )
    return response

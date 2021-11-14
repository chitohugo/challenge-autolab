
def test_get_pokemon_status_401(client, register, login):
    """
    """
    access_token = login.json["access_token"]
    response = client.get(
        '/v1/api/pokemon',
        headers={'Content-Type': 'application/json',
                 'Authorization': 'Bearer {}'.format(access_token)}
    )
    assert response.status_code == 200

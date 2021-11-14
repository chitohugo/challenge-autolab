

def test_swagger(app):
    client = app.test_client()
    response = client.get('/apidocs/')
    assert response.status_code == 200

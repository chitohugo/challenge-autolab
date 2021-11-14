
def test_create_user_success(create_user):
    """Test that a new user is created"""
    assert create_user.email == 'testing@gmail.com'


def test_create_pokemon_success(create_pokemon):
    """Test that a new pokemon is created"""
    assert create_pokemon.name == 'Bulbasaur'

from app.data.musicas import musicas
from app.data.users import users
from app.services.auth_service import authenticate_user, register_user
from app.services.musica_service import get_all_musicas


def test_register_user_adds_user_to_memory():
    user = {"email": "dj@example.com", "password": "senha123"}

    register_user(user)

    assert user in users


def test_authenticate_user_returns_matching_user():
    user = {"email": "dj@example.com", "password": "senha123"}
    register_user(user)

    assert authenticate_user("dj@example.com", "senha123") == user


def test_authenticate_user_rejects_wrong_password():
    register_user({"email": "dj@example.com", "password": "senha123"})

    assert authenticate_user("dj@example.com", "incorreta") is None


def test_get_all_musicas_returns_catalog():
    assert get_all_musicas() == musicas
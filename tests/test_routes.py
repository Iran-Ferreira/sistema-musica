from flask_jwt_extended import create_access_token

from app.data.users import users


def test_home_renders_frontend_controls(client):
    response = client.get("/")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "DJ Music System" in html
    assert 'id="registerForm"' in html
    assert 'id="loginForm"' in html
    assert 'id="getMusicasBtn"' in html
    assert "fetch('/register'" in html
    assert "fetch('/login'" in html
    assert "fetch('/musicas'" in html


def test_register_route_creates_user(client):
    response = client.post(
        "/register",
        json={"email": "dj@example.com", "password": "senha123"},
    )

    assert response.status_code == 201
    assert response.json == {"message": "Usuário cadastrado"}
    assert users == [{"email": "dj@example.com", "password": "senha123"}]


def test_login_route_returns_token_for_valid_credentials(client):
    client.post(
        "/register",
        json={"email": "dj@example.com", "password": "senha123"},
    )

    response = client.post(
        "/login",
        json={"email": "dj@example.com", "password": "senha123"},
    )

    assert response.status_code == 200
    assert response.json["token"]


def test_login_route_rejects_invalid_credentials(client):
    response = client.post(
        "/login",
        json={"email": "dj@example.com", "password": "incorreta"},
    )

    assert response.status_code == 401
    assert response.json == {"message": "Credenciais inválidas"}


def test_music_route_requires_jwt(client):
    response = client.get("/musicas")

    assert response.status_code == 401


def test_music_route_returns_catalog_with_jwt(client, app):
    with app.app_context():
        token = create_access_token(identity="dj@example.com")

    response = client.get(
        "/musicas",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "titulo": "Música A", "artista": "DJ A"},
        {"id": 2, "titulo": "Música B", "artista": "DJ B"},
    ]
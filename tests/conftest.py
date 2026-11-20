import pytest

from app import create_app
from app.data.users import users


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        TESTING=True,
        JWT_SECRET_KEY="test-secret-key",
    )
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def reset_users():
    users.clear()
    yield
    users.clear()
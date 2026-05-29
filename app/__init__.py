from flask import Flask
from flask_jwt_extended import JWTManager

from app.config import Config
from app.routes.home_routes import home_bp
from app.routes.auth_routes import auth_bp
from app.routes.musica_routes import musica_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    
    JWTManager(app)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(musica_bp)

    return app
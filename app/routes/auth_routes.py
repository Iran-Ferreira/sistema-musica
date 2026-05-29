from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.services.auth_service import (
    register_user,
    authenticate_user
)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    register_user(data)

    return jsonify(
        {"message": "Usuário cadastrado"}
    ), 201


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    user = authenticate_user(
        data["email"],
        data["password"]
    )

    if not user:
        return jsonify(
            {"message": "Credenciais inválidas"}
        ), 401

    token = create_access_token(
        identity=data["email"]
    )

    return jsonify(
        {"token": token}
    )
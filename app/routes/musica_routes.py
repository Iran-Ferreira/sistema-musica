from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.services.musica_service import (
    get_all_musicas
)

musica_bp = Blueprint(
    "musicas",
    __name__
)


@musica_bp.route("/musicas", methods=["GET"])
@jwt_required()
def listar_musicas():

    return jsonify(
        get_all_musicas()
    )
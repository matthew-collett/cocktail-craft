# api/main/routes.py
from flask import jsonify
from . import main
from api.services.cocktail_service import get_random_cocktail


@main.route('/cocktail')
def get_cocktail():
    return jsonify(status="success", cocktail=get_random_cocktail())

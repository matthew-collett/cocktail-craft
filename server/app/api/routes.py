from flask import jsonify
from server.app import api
from server.app.services import get_random_cocktail


@api.route('/cocktail')
def get_cocktail():
    return jsonify(status="success", cocktail=get_random_cocktail())

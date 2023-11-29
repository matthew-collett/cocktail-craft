# app/main/routes.py
from flask import jsonify
from . import main
from app.services import get_random_cocktail

@main.route('/')
def index():
  return jsonify(status="success", message="Cocktail Generator")

@main.route('/details')
def cocktail_details():
  return jsonify(status="success", message=get_random_cocktail())

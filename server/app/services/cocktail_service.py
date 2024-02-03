import requests
import random
from server.app.extensions import cache
from flask import current_app as app


def get_random_cocktail():
    all_cocktails = list_cocktails()
    if not all_cocktails:
        app.logger.error("No cocktails found to choose from.")
        raise ValueError("No cocktails available.")
    cocktail = random.choice(all_cocktails)
    return get_cocktail(cocktail['id'])


def get_cocktail(cocktail_id):
    url = f"{app.config.get('COCKTAIL_API_URL')}/{cocktail_id}"
    headers = get_req_headers()

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        app.logger.error(f"Error fetching cocktail with ID {cocktail_id}: {e}")
        raise


@cache.cached(timeout=300, key_prefix='all_cocktails')
def list_cocktails():
    url = app.config.get('COCKTAIL_API_URL')
    headers = get_req_headers()

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        app.logger.error(f"Error fetching cocktail list: {e}")
        raise


def get_req_headers():
    return {
        "x-rapidapi-key": app.config.get('COCKTAIL_API_KEY'),
        "x-rapidapi-host": app.config.get('COCKTAIL_API_HOST')
    }

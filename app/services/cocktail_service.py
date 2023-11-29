import requests
import random
from flask import current_app as app

def get_random_cocktail():
  all_cocktails = list_cocktails()
  cocktail = random.choice(all_cocktails)
  return get_cocktail(cocktail['id'])

def get_cocktail(id):
  url = f"{app.config.get('COCKTAIL_API_URL')}/{id}"
  headers = {
    "x-rapidapi-key": app.config.get('COCKTAIL_API_KEY'),
    "x-rapidapi-host": app.config.get('COCKTAIL_API_HOST')
  }
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    response.raise_for_status()

def list_cocktails():
  url = app.config.get('COCKTAIL_API_URL')
  headers = {
    "x-rapidapi-key": app.config.get('COCKTAIL_API_KEY'),
    "x-rapidapi-host": app.config.get('COCKTAIL_API_HOST')
  }
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    response.raise_for_status()

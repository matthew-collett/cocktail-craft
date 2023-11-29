# config.py
import os

class Config:
  COCKTAIL_API_HOST = os.getenv('COCKTAIL_API_HOST')
  COCKTAIL_API_URL = os.getenv('COCKTAIL_API_URL')
  COCKTAIL_API_KEY = os.getenv('COCKTAIL_API_KEY')
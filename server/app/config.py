import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    FLASK_ENV = os.environ.get('FLASK_ENV')
    COCKTAIL_API_HOST = os.getenv('COCKTAIL_API_HOST')
    COCKTAIL_API_URL = os.getenv('COCKTAIL_API_URL')
    COCKTAIL_API_KEY = os.getenv('COCKTAIL_API_KEY')
    CORS_HEADERS = ['Content-Type', 'Authorization']
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_MAX_AGE = 3600


class DevelopmentConfig(Config):
    DEBUG = True
    CORS_ORIGINS = os.getenv('DEV_CORS_ORIGINS').split(',')


class TestingConfig(Config):
    TESTING = True
    CORS_ORIGINS = ['*']


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    CORS_ORIGINS = os.getenv('PROD_CORS_ORIGINS').split(',')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

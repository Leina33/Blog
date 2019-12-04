import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
     DEBUG = False
     TESTING = False
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:dominic@localhost/blog'
     QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
     SECRET_KEY = os.environ.get('SECRET_KEY')
     SQLALCHEMY_TRACK_MODIFICATIONS = True
     UPLOADED_PHOTOS_DEST='app/static/photos'
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:dominic@localhost/blog'
class TestingConfig(Config):
    TESTING = True
config_options = {
'test':TestingConfig,
'production':ProductionConfig,
'development': DevelopmentConfig
}
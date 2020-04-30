import os

class Config:

  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
  
  MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  #email configurations
  MAIL_SERVER = "smtp.googlemail.com"
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  @staticmethod
  def init_app(app):
    pass

class ProdConfig(Config):
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:kimani@localhost/watchlist'
  DEBUG = True
class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:kimani@localhost/watchlist_test'

config_options = {
  'development':DevConfig,
  'production' :ProdConfig,
  'test':TestConfig
}




#before moving from the app directory
# class Config:
#   '''
#   General configuration parent class
#   '''
#   MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

# class ProdConfig(Config):
#   '''
#   Production configuration class, a child of the Config class

#   arguments:
#   Config.. the parent configuration class with the general config settings
#   '''
#   pass

# class DevConfig(Config):
#   '''
#   Development Configuration child class
  
#   Args:
#   Config: the parent configuration class with the genral config settings
#   '''

#   DEBUG = True

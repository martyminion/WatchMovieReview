import os

class Config:

  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
  
  MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:kimani@localhost/watchlist'
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  @staticmethod
  def init_app(app):
    pass

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
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

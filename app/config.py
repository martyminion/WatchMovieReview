class Config:
  '''
  General configuration parent class
  '''
  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
  '''
  Production configuration class, a child of the Config class

  arguments:
  Config.. the parent configuration class with the general config settings
  '''
  pass

class DevConfig(Config):
  '''
  Development Configuration child class
  
  Args:
  Config: the parent configuration class with the genral config settings
  '''

  DEBUG = True

class Config:
  '''
  General configuration parent class
  '''
  pass

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

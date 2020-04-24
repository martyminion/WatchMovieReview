from flask import Flask
from ..config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #initializing flask extensions
  bootstrap.init_app(app)

  #Registering the BluePrint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  # setting config
  from .request import configure_request
  configure_request(app)
   
  
  #will add the views and the forms

  return app











# from flask import Flask
# from .config import DevConfig
# from flask_bootstrap import Bootstrap

# #initializing the application
# app = Flask(__name__, instance_relative_config = True)

# #Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# #initializing bootstrap Extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error
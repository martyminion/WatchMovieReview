from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail



db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong' #offers security levels, strong checks the changes of the user request header and log him out
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)
mail = Mail()

def create_app(config_name):
  app = Flask(__name__)
  #authentication
  
  
  #creating app configurations
  app.config.from_object(config_options[config_name])
  

  config_options[config_name].init_app(app)

  #initializing flask extensions
  bootstrap.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)
  configure_uploads(app,photos)
  mail.init_app(app)
  

  #Registering the BluePrint
  from .main import main as main_blueprint
  from .auth import auth as auth_blueprint
  app.register_blueprint(main_blueprint)
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

  #setting up the login manager

  # setting config
  from .request import configure_request
  configure_request(app)
   
  
  

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
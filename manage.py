from app import db,create_app
from flask_script import Manager,Server,Shell
from app.models import User,Role,Review
from flask_migrate import Migrate,MigrateCommand

#Create app instance
#app = create_app('development')
app = create_app('production')
manager = Manager(app)
migrate = Migrate(app,db)

#create the comand that will launch the app server

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
  """Run the Unit Test"""
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User, Role = Role)

if __name__ == '__main__':
  manager.run()


  /app/.heroku/python/lib/python3.6/site-packages/flask_uploads.py
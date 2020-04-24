from app import create_app
from flask_script import Manager,Server,Shell

#Create app instance
app = create_app('development')

manager = Manager(app)

#create the comand that will launch the app server

manager.add_command('server',Server)

if __name__ == '__main__':
  manager.run()
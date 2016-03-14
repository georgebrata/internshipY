from db_manage import HelloW,Create,Upgrade,Downgrade,Migrate
from flask.ext.script import Manager
from app import app

manager = Manager(app)

manager.add_command('create',Create())
manager.add_command('upgrade',Upgrade())
manager.add_command('downgrade',Downgrade())
manager.add_command('migrate',Migrate())

@manager.command
def runserver():
    app.run(debug=True)

if __name__ == "__main__":
    manager.run()



from flask import Flask
import sqlalchemy
from flask_login import LoginManager
import logging

from models import db, Users

from index import index
from login import login
from logout import logout
from register import register
from home import home
from dashboard import dashboard

app = Flask(__name__, static_folder='../frontend/static')

app.config['SECRET_KEY'] = 'f5b2505d3af6629ae05ba2b58122cfe8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

# Registering the blueprints
app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)
app.register_blueprint(dashboard)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

if __name__ != "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    app.run()




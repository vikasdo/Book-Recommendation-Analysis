

from flask import Flask, Response
from flask_basicauth import BasicAuth
from flask_cors import CORS, cross_origin
import os

# from flask_admin import Admin, AdminIndexView
# from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from werkzeug.exceptions import HTTPException
from flask_login import LoginManager
from itsdangerous import URLSafeSerializer

# import psycopg2
# import pymysql
# import logging
# import warnings
# warnings.filterwarnings("ignore")




# Initializing Flask App
app = Flask(__name__)



app.secret_key="Vampire"

# This video demonstrates why we use CORS in our Flask App - https://www.youtube.com/watch?v=vWl5XcvQBx0
CORS(app)


app.config.from_object("config.DevelopmentConfig")


# Creating and Initializing db object of SQLAlchemy class
db = SQLAlchemy(app)
db.init_app(app)



SQLITE_DB_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'db.sqlite')


migrate = Migrate(app, db, render_as_batch=True)

with app.app_context():
	if db.engine.url.drivername == 'sqlite':
		migrate.init_app(app, db, render_as_batch=True)
	else:
		migrate.init_app(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


"""
Creating basic_auth object of BasicAuth class.
We are using BasicAuth only to protect our Admin pages.

WARNING:
We implemented BasicAuth when this App was in early stage.
This is not a full-fledged authentication and
authorization system for our admin panel.

It is recommended to replace BasicAuth with a
proper authentication system using Flask-Login,
the way we have for our client users.
"""
basic_auth = BasicAuth(app)

# Creating serializer object of URLSafeSerializer class for serializing session_token
serializer = URLSafeSerializer(app.secret_key)



# Creating login_manager object of LoginManager class for implementing Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.init_app(app)


# Here we set session_token as our user_loader.
@login_manager.user_loader
def load_user(session_token):
	return User.query.filter_by(session_token=session_token).first()

from bookstore.client.views import client

app.register_blueprint(client)
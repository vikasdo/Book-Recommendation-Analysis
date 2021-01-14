

from flask import Flask, Response
from flask_basicauth import BasicAuth
from flask_cors import CORS, cross_origin
import os

# from flask_admin import Admin, AdminIndexView
# from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy  as _BaseSQLAlchemy
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


class SQLAlchemy(_BaseSQLAlchemy):
	"""
	This class is defined so that we can set "pool_pre_ping" to True.
	pool_pre_ping is a boolean flag, which when set to True,
	will enable the connection pool 'pre-ping' feature
	that tests connections for liveness upon each checkout.
	
	This prevents from dropping of database connection with our app.
	This class inherits the original SQLAlchemy class,
	and nothing else is changed except pool_pre_ping flag
	https://docs.sqlalchemy.org/en/13/core/pooling.html#dealing-with-disconnects
	https://github.com/pallets/flask-sqlalchemy/issues/589
	"""
	def apply_pool_defaults(self, app, options):
		super(SQLAlchemy, self).apply_pool_defaults(app, options)
		options["pool_pre_ping"] = True
# Creating and Initializing db object of SQLAlchemy class
db = SQLAlchemy(app)
db.init_app(app)





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





# Here we set session_token as our user_loader.

from bookstore.client.views import client

app.register_blueprint(client)
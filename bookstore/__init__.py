

from flask import Flask, Response
from flask_basicauth import BasicAuth
from flask_cors import CORS, cross_origin
import os
import nltk
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from werkzeug.exceptions import HTTPException
from flask_login import LoginManager
from itsdangerous import URLSafeSerializer
import psycopg2
import pymysql
import logging
import warnings
warnings.filterwarnings("ignore")




# Initializing Flask App
app = Flask(__name__)



# This video demonstrates why we use CORS in our Flask App - https://www.youtube.com/watch?v=vWl5XcvQBx0
CORS(app)




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

# Creating login_manager object of LoginManager class for implementing Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'client.login'
login_manager.init_app(app)


# Here we set session_token as our user_loader.
@login_manager.user_loader
def load_user(session_token):
	return User.query.filter_by(session_token=session_token).first()

"""
The following three classes are inherited from their respective base class,
and are customized, to make flask_admin compatible with BasicAuth.

The following link described the problem and solution.
https://stackoverflow.com/questions/54834648/flask-basicauth-auth-required-decorator-for-flask-admin-views
"""
class AuthException(HTTPException):
	def __init__(self, message):
		super().__init__(message, Response(
			"You could not be authenticated. Please refresh the page.", 401,
			{'WWW-Authenticate': 'Basic realm="Login Required"'} ))

class MyModelView(ModelView):
	def is_accessible(self):
		if not basic_auth.authenticate():
			raise AuthException('Not authenticated.')
		else:
			return True
	def inaccessible_callback(self, name, **kwargs):
		return redirect(basic_auth.challenge())

class MyAdminIndexView(AdminIndexView):
	def is_accessible(self):
		if not basic_auth.authenticate():
			raise AuthException('Not authenticated.')
		else:
			return True
	def inaccessible_callback(self, name, **kwargs):
		return redirect(basic_auth.challenge())

# Creating admin object of Admin class to implement flask_admin
admin = Admin(app, index_view=MyAdminIndexView(url='/kUQqQm9geK'), name='Admin', template_mode='bootstrap3')


# Importing models from models.py to register them on Admin Panel
from reviewcruncher.models import Company, User, FinalSuggestions, CompetitorAnalysis, CompetitorRelation,CustomizationOfFeatures

"""
Here we register our models using add_view method so that,
the database tables can be viewed from Flask Admin Panel.

If any new models are created then it is recommended to import them,
and then register them here, so that the Admin can view them in Admin Panel
"""
admin.add_view(MyModelView(Company, db.session, category='Database Overview'))
admin.add_view(MyModelView(User, db.session, category='Database Overview'))
admin.add_view(MyModelView(FinalSuggestions, db.session, category='Database Overview'))
admin.add_view(MyModelView(CompetitorRelation, db.session, category='Database Overview'))
admin.add_view(MyModelView(CompetitorAnalysis, db.session, category='Database Overview'))
admin.add_view(MyModelView(CustomizationOfFeatures, db.session, category='Database Overview'))


"""
Here we import our blueprints and register them using
register_blueprint method, so that the routes defined in
respective blueprint packages can be accessed from here.

If any new blueprint packages are created then it is required
to import and register them here.
"""
from reviewcruncher.admin.views import myadmin
from reviewcruncher.client.views import client

app.register_blueprint(myadmin, url_prefix='/kUQqQm9geK')
app.register_blueprint(client)
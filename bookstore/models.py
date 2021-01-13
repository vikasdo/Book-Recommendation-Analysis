from bookstore import db
from flask_login import UserMixin


"""
These are all the Models which we are currently using in our App.
"""


class User(UserMixin, db.Model):
	__table_args__ = (
        db.UniqueConstraint('email', 'id', name='unique_component_commit'),
    )
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	password = db.Column(db.String(255), nullable=False)

	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return f"User('{self.id}','{self.name}','{self.email}','{self.company}')"
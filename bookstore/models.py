from bookstore import db
from flask_login import UserMixin
from datetime import datetime

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

	location = db.Column(db.String(255), nullable=False)
	age = db.Column(db.String(255))

	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return f"User('{self.id}','{self.name}','{self.email}')"

class Books(db.Model):
	bid = db.Column(db.Integer,primary_key=True)
<<<<<<< HEAD
	ISBN = db.Column(db.String(100),nullable=False)
=======
	ISBN = db.Column(db.String(10),nullable=False)
>>>>>>> 6e2965e1655c2a4423d75ac6e360b4d22b68cc28
	title = db.Column(db.String(255),nullable=False)
	author = db.Column(db.String(100),nullable=False)
	publisher = db.Column(db.String(100),nullable=False)
	book_cost = db.Column(db.String(100),nullable=False)
<<<<<<< HEAD
	pubDate = db.Column(db.String(20),nullable=False,default="2001")
=======
	pubDate = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
>>>>>>> 6e2965e1655c2a4423d75ac6e360b4d22b68cc28
	bookImage = db.Column(db.String(500),nullable=False)

	def __repr__(self):
		return f"Books('{self.ISBN}','{self.title}','{self.bookImage}','{self.book_cost}')"
'''
class Cart(UserMixin,db.Model):
	cart_id = db.Column(db.Integer,primary_key=True)
	total_amount = db.Column(db.Integer,nullable=False)

class Payment(UserMixin,db.Model):
	payment_id = db.Column(db.Integer,primary_key=True)
	cart_id = db.relationship()
	user_id = db.relationship()
	payment_type = db.Column(db.String(255),nullable=False,default="Online")

'''



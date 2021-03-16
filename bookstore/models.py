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
	#user_rating = db.relationship('Ratings',backref="user_id",uselist=False)

	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return f"User('{self.id}','{self.name}','{self.email}')"

class Books(db.Model):
	bid = db.Column(db.Integer,primary_key=True)
	ISBN = db.Column(db.String(50),nullable=False)
	title = db.Column(db.String(255),nullable=False)
	author = db.Column(db.String(100),nullable=False)
	publisher = db.Column(db.String(100),nullable=False)
	book_cost = db.Column(db.String(100),nullable=False)
	pubDate = db.Column(db.String(20),nullable=False,default="2001")
	bookImage = db.Column(db.String(500),nullable=False)
	#book_rating = db.relationship('Ratings',backref="book_id",uselist=False)

	def __repr__(self):
		return f"Books('{self.ISBN}','{self.title}','{self.bookImage}','{self.book_cost}')"

class offer(db.Model):
	offerid = db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
	discount=db.Column(db.Integer,default=0,nullable=False)

	def get_json(self):
		return { self.user_id:self.discount}

class Ratings(db.Model): 
	rid = db.Column(db.Integer,primary_key=True)
	rating = db.Column(db.Integer,default=0) 
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
	book_id = db.Column(db.String(100),db.ForeignKey('books.ISBN'))
	
	def __repr__(self):
		return f"Ratings('{self.book_id}','{self.user_id}','{self.rating}')"

'''
class Cart(db.Model):
	cid = db.Column(db.Integer,primary_key=True)
	book_id = db.Column(db.Integer,db.ForeignKey('books.bid'))
	quantity = db.Column(db.Integer,nullable=False)
	#transaction = db.Column(db.Integer,db.ForeignKey('transaction.tid')) # the tid involved
'''
# it will have many cart items and total price

class OrderList(db.Model):
	tid = db.Column(db.Integer,primary_key=True)
	book_ISBN = db.Column(db.String(100),db.ForeignKey('books.bid'))
	quantity = db.Column(db.Integer,nullable=False)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
	total_price = db.Column(db.Integer,nullable=False)


'''



ORDERS
	
	SELECT book_ISBN,SUM(quantity)*110 as revenue from order_list 
	group by(book_ISBN) ORDER BY revenue DESC LIMIT 5

RATINGS 

	SELECT book_id,AVG(rating) as red from ratings group by(book_id) ORDER BY red DESC TOP 4

USERS LOCATION GROUP BY

	SELECT us.email,us.location from user us,order_list ol where ol.user_id=us.id group by(us.location) order by count(location) DESC 

AVG RATING IN GIVEN LOCATION
	

'''
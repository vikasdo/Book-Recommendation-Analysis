import datetime
from bookstore import db
from bookstore.models import OrderList, Books
from flask_sqlalchemy import SQLAlchemy



#start of the month
def calc_start(y, m):
	return datetime.datetime(y, m, 1)

#end of the month
def calc_end(y, m):
	if m == 2:
		if (y % 4) == 0:
			if (y % 100) == 0:
				if (y % 400) == 0:
				   return datetime.datetime(y, m, 29, 23, 59, 59)
				else:
				   return datetime.datetime(y, m, 28, 23, 59, 59)
			else:
				return datetime.datetime(y, m, 29, 23, 59, 59)
		else:
			return datetime.datetime(y, m, 28, 23, 59, 59)
	else:
		if m <= 7:
			if m % 2 == 0:
				return datetime.datetime(y, m, 30, 23, 59, 59)
			else:
				return datetime.datetime(y, m, 31, 23, 59, 59)
		else:
			if m % 2 == 0:
				return datetime.datetime(y, m, 31, 23, 59, 59)
			else:
				return datetime.datetime(y, m, 30, 23, 59, 59)


def total_sales_bw_b_e_admin(begin="2021-05-01", end="2021-05-31"):
	return db.session.query(db.func.sum(OrderList.total_price)).filter(OrderList.selling_date >= begin, OrderList.selling_date <= end).scalar()


def total_books_bw_b_e_admin(book_id):
	try:
		return db.session.query(db.func.sum(OrderList.total_price)).filter(OrderList.book_ISBN == book_id).scalar()
	except:
		return 0

#total sales calculation
def calc_sales(y):
	sales_yearly = list()
	for i in range(1, 13):
		beg = calc_start(y, i)
		en = calc_end(y, i)
		temp = total_sales_bw_b_e_admin(beg, en)
		if temp is None:
			temp = 0
		sales_yearly.append(temp)
	return sales_yearly

#for book wise sales
def book_wise():
	books_yearly = dict()
	for i in OrderList.query.with_entities(OrderList.book_ISBN).distinct():
		temp = total_books_bw_b_e_admin(int(i[0]))
		if temp is None:
			temp = 0
		book = Books.query.filter_by(bid=int(i[0])).first()
		title = book.title
		books_yearly[title] = temp
	return books_yearly

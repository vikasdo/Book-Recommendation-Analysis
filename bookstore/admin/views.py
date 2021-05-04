from flask import Flask, render_template, url_for, request, redirect, flash, session, Blueprint
from bookstore.models import User, Books, Ratings, OrderList, offer, Contact
from bookstore import db, serializer, app
from bookstore.admin.admin_credentials import admin_password, admin_username
from functools import wraps
import datetime
from flask_sqlalchemy import SQLAlchemy
from bookstore.admin import admin_functions


admin = Blueprint('admin', __name__)




##custom decorators
#check if admin is logged in or not based on session
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_in' not in session:
            return redirect(url_for('admin_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


##routes
#index of admin
@app.route('/admin/')
@login_required
def admin_index():
    year = datetime.datetime.now().year
    sales_yearly = admin_functions.calc_sales(year)
    books_yearly = admin_functions.book_wise()
    return render_template('admin/index.html', year=year, sales_yearly=sales_yearly, total=sum(sales_yearly), books_yearly=books_yearly)


#add book
@app.route('/admin/addbook', methods = ['GET', 'POST'])
@login_required
def admin_add_book():
    if request.method == 'GET':
        return render_template('admin/add_book.html')
    else:
        title = request.form.get('Book_title')
        ISBN = request.form.get('ISBN')
        author = request.form.get('author')
        publisher = request.form.get('publisher')
        img = request.form.get('Book_img')
        pub_date = request.form.get('pub_date')
        pub_date = datetime.datetime.strptime(pub_date, '%Y-%m-%d')
        Book_cost = request.form.get('Book_cost')
        book = Books(ISBN = ISBN, title = title, author = author, publisher = publisher, book_cost = Book_cost, pubDate = pub_date.date(), bookImage = img)
        db.session.add(book)
        db.session.commit()
        flash('book added successfully', 'info')
        return redirect(url_for('admin_add_book'))


# admin login
@app.route('/admin/login', methods = ['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:
        username = request.form.get('admin_username')
        password = request.form.get('admin_password')
        if username == admin_username and password == admin_password:
            session['admin_in'] = True
            flash('Logged in Successfully as admin',category='success')
            return redirect(url_for('admin_index'))
        else:
            flash('Wrong credentials', category='error')
            return redirect(url_for('admin_login'))


# admin logout
@app.route('/admin/logout')
@login_required
def admin_logout():
    session.pop('admin_in', None)
    flash('logged out', category='info')
    return redirect(url_for('admin_login'))

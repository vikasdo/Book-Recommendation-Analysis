from flask import Flask, render_template, url_for, request, redirect, flash, session, Blueprint
from bookstore.models import User, Books, Ratings, OrderList, offer, Contact
from bookstore import db, serializer, app
from bookstore.admin.admin_credentials import admin_password, admin_username
from functools import wraps
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from bookstore.admin import admin_functions


admin = Blueprint('admin', __name__)


#flask mail config
app.config["MAIL_DEFAULT_SENDER"] = "bookly1120@gmail.com"
app.config["MAIL_PASSWORD"] = "bookly@112000"
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "bookly1120"
mail = Mail(app)


##custom decorators
#check if admin is logged in or not based on session variable2
def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_in' not in session:
            return redirect(url_for('admin_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


##routes
#index of admin
@app.route('/admin/')
@admin_login_required
def admin_index():
    year = datetime.datetime.now().year
    sales_yearly = admin_functions.calc_sales(year)
    books_yearly = admin_functions.book_wise()
    return render_template('admin/index.html', year=year, sales_yearly=sales_yearly, total=sum(sales_yearly), books_yearly=books_yearly)


#add book
@app.route('/admin/addbook', methods = ['GET', 'POST'])
@admin_login_required
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


#contact request
@app.route('/admin/contact_request', methods = ['POST', 'GET'])
@admin_login_required
def admin_contact_request():
    if request.method == 'POST':
        if request.form.get('reply'):
            cid = request.form.get('reply')
            contact_to_reply = Contact.query.filter_by(cid = cid).first()
            session['reply_email'] = contact_to_reply.email
            return render_template('admin/reply_contact_request.html', contact = contact_to_reply)
        else:
            cid = request.form.get('delete')
            contact_to_be_del = Contact.query.filter_by(cid = cid).first()
            db.session.delete(contact_to_be_del)
            db.session.commit()
            return redirect(url_for('admin_contact_request'))
    to_contact = Contact.query.filter_by().all()
    return render_template('admin/contact_request.html', to_contact = to_contact)


#reply via email
@app.route('/admin/contact_reply', methods = ['POST'])
@admin_login_required
def admin_contact_reply():
    reply_message = request.form.get('reply_message')
    try:
        message = Message("Reply to Contact query from Bookly!!",
                        sender='bookly1120@gmail.com', recipients=[session['reply_email']])
        message.body = reply_message
        mail.send(message)
        flash(f'Email sent.', 'success')
    except:
        flash(f'Error sending email.', 'error')
    return redirect(url_for('admin_contact_request'))


# admin logout
@app.route('/admin/logout')
@admin_login_required
def admin_logout():
    session.pop('admin_in', None)
    flash('logged out', category='info')
    return redirect(url_for('admin_login'))

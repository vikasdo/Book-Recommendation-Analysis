import flask
from flask import render_template, url_for, request, redirect, flash, session, jsonify, Blueprint ,Response
from flask_login import login_required, current_user, login_user, logout_user,login_manager,LoginManager
from werkzeug.security import check_password_hash
from datetime import datetime
# import pandas as pd
import glob,json,re
import os,pickle,collections
from bookstore.models import User,Books,Ratings
from bookstore import db, serializer, app
from werkzeug.security import generate_password_hash
from bookstore.client.recommendation_engine import Recommendation_engine
# create A Blueprint

client = Blueprint('client', __name__)


# Creating login_manager object of LoginManager class for implementing Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.init_app(app)


@app.route('/')
@login_required
def home():
    books = Books.query.limit(15).all()
    return  render_template("client/index.html",books=books)


@app.route('/login' , methods=['GET' , 'POST'])
def login():

    if current_user.is_authenticated:
        flash('Already Logged in...','info')
        return redirect(url_for('home'))


    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        ok = User.query.filter_by(email=email).first()
        if ok is not None:
            login_user(ok)
            flash("Login Success :)",'success')
            return redirect(url_for('home'))
        else:
            flash("Email doesn't exit, Signup First...",'error')
            return redirect(url_for('register'))

    return render_template('client/login.html')

@app.route('/register' , methods = ['GET' , 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email =request.form['email']
        password = request.form['password']
        location = request.form['location']
        age = request.form['age']

        ok = User.query.filter_by(email=email).first()

        if ok:
            flash('Existing User Login to continue...','error')
            return redirect(url_for('login'))

        new_user =  User(name=username,email=email,
                        password=generate_password_hash(password, method='sha256'), location = location, age = age)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account Created for {username}','success')
        return redirect(url_for('login'))
    else:
        return render_template('client/signup.html')



@app.route('/admin/addBook',methods=['GET','POST'])
def addBook():
    if request.method =='POST':
        data = request.form;

        title = data['title']
        publisher = data['publisher']
        author = data['author']
        bookcost = data['book_cost']
        imageURL = data['imageURL']

        ok = Books(title=title,publisher=publisher,author=author,book_cost=bookcost,bookImage = imageURL)

        db.session.add(ok)
        db.session.commit()
        flash(f'Book with title {title} added successfully','success')
        return redirect(url_for('addBook'))

    return render_template('client/adminBook.html')

@app.route('/single_product/<string:bookid>',methods = ['GET','POST'])
@login_required
def single_product(bookid):


    if request.method=='POST':

        user_id=request.form.get('user_id')
        user_rating= request.form.get('user_rating')
        book_id = request.form.get('book_id')

        es=len(book_id)

        if(book_id[es-1]=='!' and book_id[es-2]=='#'):
            book_id=book_id[:es-2]

        print(book_id)

        ok = Ratings.query.filter_by(user_id=user_id).first();

        if not ok: 

            red = Ratings(user_id=user_id,rating=user_rating,book_id=book_id)
            db.session.add(red)
            db.session.commit();

        else:
            ok.rating=user_rating

        print(Ratings.query.all())
       

    books = Books.query.filter_by(ISBN=bookid).first() 
    #call to recommendation engine
    print(current_user.id)

    user_id=current_user.id;
    pickle_file="filename.pickle"
    
    with open(pickle_file,'rb') as infile:
        pickled_data = pickle.load(infile)

    out=None
    if user_id  not in pickled_data:
        Recommendation_engine_obj=Recommendation_engine()
        out=Recommendation_engine_obj.getRecommendedBooks(user_id)
        pickled_data[user_id]=out
    else:
        out=pickled_data[user_id]
       
    filename = "filename.pickle"
    outfile = open(filename,'wb')
    pickle.dump(pickled_data,outfile)
    outfile.close()
    return render_template('client/single.html',books=books,suggestedBooks=out)


@app.route('/myprofile')
@login_required
def myprofile():
    return render_template('client/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('See you later','success')
    return render_template('client/login.html')



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
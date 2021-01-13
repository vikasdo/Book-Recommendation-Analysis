import flask
from flask import render_template, url_for, request, redirect, flash, session, jsonify, Blueprint ,Response
from flask_login import login_required, current_user, login_user, logout_user,login_manager,LoginManager
from werkzeug.security import check_password_hash
from datetime import datetime
# import pandas as pd
import glob,json,re
import os,pickle,collections
from bookstore.models import User
from bookstore import db, serializer, app
from werkzeug.security import generate_password_hash
# create A Blueprint

client = Blueprint('client', __name__)


# Creating login_manager object of LoginManager class for implementing Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.init_app(app)


@app.route('/')
@login_required
def home():
    return  render_template("client/index.html")


@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        print('Logged in..')

        ok = User.query.filter_by(email=email).first()

        login_user(ok)
        return redirect(url_for('home'))
        
    else:
        return render_template('client/login.html')

@app.route('/register' , methods = ['GET' , 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['username']
        email =request.form['email']
        password = request.form['password']
        new_user =  User(name=username,email=email,
                        password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('client/signup.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
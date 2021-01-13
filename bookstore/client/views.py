import flask
from flask import render_template, url_for, request, redirect, flash, session, jsonify, Blueprint ,Response
from flask_login import login_required, current_user, login_user, logout_user
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

@app.route('/')
def home():
    return  render_template("client/index.html")


@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']
        print('Logged in..')
        # login_user()
        return redirect(url_for('home'))
        
    else:
        return render_template('client/login.html')

@app.route('/register' , methods = ['GET' , 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']
        new_user =  User(name=name,email=email,
                        password=generate_password_hash(password, method='sha256'),
                        session_token='123')
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        new_user =  User(name='vikas',email='asnsa',
                        password=generate_password_hash('121', method='sha256'),
                        session_token='123')
        db.session.add(new_user)
        db.session.commit()
        return render_template('client/signup.html')
import flask
from flask import render_template, url_for, request, redirect, flash, session, jsonify, Blueprint ,Response
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import check_password_hash
from datetime import datetime
# import pandas as pd
import glob,json,re
import os,pickle,collections
from models import User
from bookstore import db, serializer, app

# create A Blueprint

#client = Blueprint('client', __name__)


@app.route('/home')
@login_required
def home():
    return  render_template("client/index.html")


@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if registeredUser != None and registeredUser.password == password:
            print('Logged in..')
            login_user(registeredUser)
            return redirect(url_for('home'))
        else:
            return abort(401)
    else:
        return render_template('client/login.html')

@app.route('/register' , methods = ['GET' , 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username , password , users_repository.next_index())
        users_repository.save_user(new_user)
        return redirect(url_for('login'))
    else:
        return render_template('client/signup.html')
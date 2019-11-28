from flask import render_template,redirect
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html' , form = loginform)
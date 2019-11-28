from flask import render_template,redirect,url_for
from . import auth
from .. import User
from .. import db
from .forms import RegForm,LoginForm 

@auth.route('/login')
def login():
    return render_template('auth/login.html' , form = loginform)

@auth .route('/registration')
def registration():
    form =RegForm
    if form.validate_on_submit():
        user = User(email = form.email.data,username = form.username.data,password = form.password.data)

        db.session.add(user)
        db.commit()
        return redirect(url_for('auth.login'))
        title = 'registration'
    return render_template('auth/registration.html', regform =form)

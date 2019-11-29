from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .. import db
from .forms import RegForm,LoginForm 
from flask_login import login_user,login_required,logout_user


@auth.route('/login',methods = ["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(url_for('main.index') or request.args.get('next'))

        flash('invalid Username or Password')

    title = 'Blog login'
    return render_template('auth/login.html' ,title=title, loginform = form)

@auth .route('/registration',methods = ['GET','POST'])
def registration():
    form =RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,username = form.username.data,password = form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'registration'
    return render_template('auth/registration.html', regform =form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
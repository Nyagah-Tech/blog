from flask_login import login_required,current_user
from flask import render_template,redirect,url_for,abort
from .. import db
from ..models import User
from . import main

@main.route('/')
def index():
    title ="home"

    return render_template('index.html',title=title)

@main.route('blog/new/<uname>', methods = ["GET","POST"])
@login_required
def new_blog(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form =NewBlog()
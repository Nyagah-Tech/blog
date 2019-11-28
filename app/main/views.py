from flask_login import login_required,current_user
from flask import render_template,redirect,url_for,abort
from .. import db
from ..models import User,Blog
from . import main
from .forms import New_blog_form

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
    form = New_blog_form()
    if form.validate_on _submit():
        title = form.title.data
        body = form.title.data
        
        new_blog = Blog(blog_title = title,blog_body = body,user = current_user.username)

        new_blog.save_blog()
        return redirect(url_for('.profile', uname = current_user.username))

    title = 'new pitch'
    return render_template('new_blog.html',title = title, newBlog_form = form)
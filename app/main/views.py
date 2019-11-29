from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog
from .forms import New_blog_form
from .. import db

@main.route('/')
def index():
    title ="home"

    return render_template('index.html',title=title)

@main.route('/blog/new/<uname>', methods = ['GET','POST'])
@login_required
def new_blog(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = New_blog_form()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        
        new_blog = Blog(blog_title = title,blog_body = body,user = current_user.username)

        new_blog.save_blog()
        return redirect(url_for('.profile', uname = current_user.username))

    title = 'new pitch'
    return render_template('new_blog.html',title = title, newBlog_form = form)

@main.route('/blog/user/profile/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    bloglist = Blog.get_user_blog(user.username)
    return render_template("profile/profile.html",user = user, bloglist = bloglist)


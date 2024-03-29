from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Subscribe
from .forms import New_blog_form,CommentForm,UpdateProfileForm,UpdateBlogForm,Subscribe_Form
from .. import db,photos
from ..email import mail_message
from ..requests import get_quotes

@main.route('/')
def index():
    title ="home"

    quotes = get_quotes()

    blogs = Blog.get_all_blog()

    return render_template('index.html',title=title,quotes =quotes,blogs = blogs)

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
        email_list = Subscribe.get_all_email()
        for emails in email_list:
            mail_message("Your daily newsfeed","email/subscription_user",emails.email,emails = emails)


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

@main.route('/blog/profile/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    form = CommentForm()
    blog = Blog.query.filter_by(id = id).first()
    if form.validate_on_submit():
        comment = form.body.data

        new_comment = Comment(user = current_user.username,blog_comment = comment,blog_id = blog.id)

        new_comment.save_comment()
        return redirect(url_for('.blog',id = blog.id))

    title = 'comments'
    return render_template('comment.html',title = title,comment_form =form,blog = blog)


@main.route('/blog/<id>')
@login_required
def blog(id):
    blog = Blog.query.filter_by(id = id).first()
    comment = Comment.get_comment(id)
    return render_template('blog.html',blog = blog, comment = comment)

@main.route('/profile/update/<uname>', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfileForm()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/updateProf.html',updateForm = form,)


@main.route('/profile/<uname>/update/profile/pic/', methods = ['Post'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in  request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = user.username))


@main.route('/blog/delete/<int:id>', methods = ['GET','POST'])
@login_required
def delete_blog(id):
    blog = Blog.query.filter_by(id = id).first()
    Blog.delete_blog(blog)

    return redirect(url_for('main.profile', uname = current_user.username))

@main.route('/blog/update/<int:id>',methods = ['GET','POST'])
@login_required
def update_blog(id):
    blog = Blog.query.filter_by(id = id).first()
    form = UpdateBlogForm()

    if form.validate_on_submit():
        blog.blog_title = form.title.data
        blog.blog_body = form.body.data

        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.profile', uname = current_user.username))

    return render_template('profile/updateBlog.html',updateblogform = form)
    
    
@main.route('/user/subcribe/<uname>', methods = ['GET','POST'])
@login_required
def subcribe(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = Subscribe_Form()

    if form.validate_on_submit():
        email = form.email.data
        username= form.username.data

        new_sub = Subscribe(username = username,email = email)
        db.session.add(new_sub)
        db.session.commit()

        return redirect(url_for('.index'))


    return render_template('subscribe/subscribe.html',subcribeForm = form,user = user)

@main.route('/comment/delete/<int:id>')
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id = id).first()
    
    Comment.delete_comment(comment)

    return redirect(url_for('.blog', id = comment.blog_id))





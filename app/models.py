from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(30),index = True)
    email = db.Column(db.String(),unique = True,index = True)
    pass_code = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('Access denied.Read acess is permitted')
    @password.setter
    def password(self, password):
        self.pass_code = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_code,password)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    user = db.Column(db.String)
    blog_title = db.Column(db.String)
    blog_body = db.Column(db.String)
    posted = db.Column(db.DateTime,default = datetime.utcnow)

    def save_blog(self):
        db.session(self)
        db.session.commit()

    @classmethod
    def get_user_blog(cls,name):
        blog = Blog.query.filter_by(user = name)

        return blog

    @classmethod
    def get_all_blog(cls):
        blod_list = Blog.query.all()
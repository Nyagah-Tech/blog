from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(30),index = True)
    email = db.Column(db.String(),unique = True,index = True)
    pass_code = db.Column(db.String(16))


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



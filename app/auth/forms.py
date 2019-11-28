from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    username = StringField('your username',validators = [Required()])
    password = PasswordField('Your password...',validators = [Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')

class RegForm(FlaskForm):
    email = StringField('your email',validators = [Email(),Required()])
    username = StringField('your username', validators = [Required()])
    password = PasswordField('your password',validators =[Required(),EqualTo('password_confirm',message = 'Password must match')])
    password_confirm = PasswordField('Confirm password',validators = [Required()])
    submit = SubmitField('Submit')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account registered with that email')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('The username exists..')


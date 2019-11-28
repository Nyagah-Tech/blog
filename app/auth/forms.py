from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    username = StringField('your username',validators = [Required()])
    password = PasswordField('Your password...',validators = [Required()])
    submit = SubmitField('Submit')

class RegForm(FlaskForm):
    email = StringField('your email',validators = [Email(),Required()])
    username = StringField('your username', validators = [Required()])
    password = PasswordField('your password',validators =[Required(),EqualTo('password_confirm',message = 'Password must match')])
    password_confirm = PasswordField('Confirm password',validators = [Required()])

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.field).first():
            raise ValidationError('There is an account registered with that email')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.field).first():
            raise ValidationError('The username exists..')

            
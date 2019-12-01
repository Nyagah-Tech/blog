from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,TextAreaField,SubmitField
from wtforms.validators import Required,Email

class New_blog_form(FlaskForm):
    title = StringField('Blog title',validators = [Required()])
    body = TextAreaField('Write your blog here ', validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    body = TextAreaField('write your comment', validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfileForm(FlaskForm):
    bio = StringField('write your bio',validators = [Required()])
    submit = SubmitField('Submit')

class UpdateBlogForm(FlaskForm):
    title = StringField('Blog title', validators = [Required()])
    body = TextAreaField('write your blog here..',validators = [Required()])
    submit = SubmitField('Submit')

class Subscribe_Form(FlaskForm):
    email = StringField('your email',validators = [Required(),Email()])
    username = StringField('your username',validators = [Required()])
    submit = SubmitField('Submit')
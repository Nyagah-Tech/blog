from flask_login import login_required,current_user
from flask import render_template,redirect,url_for
from .. import db
from ..models import User
from . import main

@main.route('/')
def index():
    title ="home"

    return render_template('index.html',title=title)
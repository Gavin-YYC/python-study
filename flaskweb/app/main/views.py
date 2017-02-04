# coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask_login import current_user

from . import main
from .. import db
from ..models import User

@main.route('/')
def index():
    return render_template('index.html', current_user=current_user)

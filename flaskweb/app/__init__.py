# coding=utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# 这个必须要放到下面执行，否则获取不到上述变量
from .main import main as main_blueprint
from .auth import auth as auth_blueprint

def create_app( config_name ):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app( app )

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    bootstrap.init_app( app )
    mail.init_app( app )
    moment.init_app( app )
    db.init_app( app )
    login_manager.init_app( app )

    return app

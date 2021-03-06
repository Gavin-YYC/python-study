# coding=utf-8

from flask import request, render_template, redirect, url_for, flash
from . import auth
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, current_user,login_required
from ..models import User
from .. import db
from ..email import send_email

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid email or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect( url_for('main.index') )

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
            username = form.username.data,
            password = form.password.data)
        db.session.add( user )
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm your Account', 'auth/email/confirm', user=user, token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect( url_for('main.index') )
    return render_template('auth/register.html', form=form)

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm your Account', 'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been send to you by email.')
    return redirect( url_for('main.index') )

@auth.route('/confirm/<token>')
def confirm( token ):
    if current_user.confirmed:
        return redirect( url_for('main.index') )
    if current_user.confirm( token ):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired')
    return redirect( url_for('main.index') )

@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
        return redirect( url_for('auth.unconfirmed') )

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect( url_for('main.index') )
    return render_template('auth/unconfirmed.html')

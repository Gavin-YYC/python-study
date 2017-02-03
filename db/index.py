# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath( os.path.dirname( __file__ ) )

app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join( basedir, 'data.sqlite' )

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy( app )


class Role( db.Model ):
    __tablename__ = 'roles'
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String( 64  ), unique = True )

    users = db.relationship( 'User', backref = 'role' )

    def __repr__( self ):
        return '<Role {name}'.format( name = self.name )


class User( db.Model ):
    __tablename__ = 'users'
    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String( 64 ), unique = True, index = True )

    role_id = db.Column( db.Integer, db.ForeignKey('roles.id') )

    def __repr__( self ):
        return '<User {username}'.format( username = self.username )

@app.route('/', methods=['GET', 'POST'])
def index():
    user = 'Hello'
    if user is None:
        user = User(username = 'john')
        db.session.add( user )
    else:
        user = User.query.filter_by( username = 'john' ).first()
    return user

if __name__ == '__main__':
    app.run()

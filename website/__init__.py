from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():

  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'sitammisary'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  with app.app_context():  # Add app.app_context() here
      from website import auth, views
      app.register_blueprint(views.views, url_prefix='/')
      app.register_blueprint(auth.auth, url_prefix='/')

      from .models import User, Transaction, Account
      create_database(app)

  return app


def create_database(app):
  if not path.exists('website/' + DB_NAME):
    db.create_all()
    print("Created database!")
    
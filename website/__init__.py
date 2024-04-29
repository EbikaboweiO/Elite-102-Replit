from flask import Flask
import sqlite3
from os import path

DB_NAME = 'database.db'

def create_app():
  # configuring the app here
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'sitammisary'
  # app config so I can if there are any bugs I need to fix
  app.config['DEBUG'] = True
  
  with app.app_context():  
      from website import auth, views

      app.register_blueprint(views.views, url_prefix='/')
      app.register_blueprint(auth.auth, url_prefix='/')

      from .models import Account, Transactions, User

      create_database(app)

  return app


def create_database(app):
  if not path.exists('website/' + DB_NAME):
    conn = sqlite3.connect('website/' + DB_NAME)
    c = conn.cursor()

    # Creating tables
    c.execute('''CREATE TABLE IF NOT EXISTS account
                 (id INTEGER PRIMARY KEY, name TEXT, balance REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY, account_id INTEGER, amount REAL, timestamp TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        first_name TEXT
    )''')
    print("User table created successfully")

    conn.commit()
    conn.close()
    print("Created database!")

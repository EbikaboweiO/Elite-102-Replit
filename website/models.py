from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  first_name = db.column(db.String(150))

  def __init__(self, email, first_name, password):
    self.email = email
    self.first_name = first_name
    self.password = password

class Transaction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  amount = db.Column(db.Float)
  date = db.Column(db.DateTime)
  description = db.Column(db.String(500))
  category = db.Column(db.String(50))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def deposit_funds(self, amount):
        self.balance += amount
        db.session.commit()

    def withdraw_funds(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            db.session.commit()
        else:
            raise ValueError('Insufficient funds')

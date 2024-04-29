# class for the user's account
class Account:
  def __init__(self, id, name, balance):
    self.id = id
    self.name = name
    self.balance = balance

# class for transactions so that they can be stored and the such
class Transactions:
  def __init__(self, id, account_id, amount, timestamp):
    self.id = id
    self.account_id = account_id
    self.amount = amount
    self.timestamp = timestamp

# class for the user
class User:
  def __init__(self, id, username, password):
    self.id = id
    self.username = username
    self.password = password
    
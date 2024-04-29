from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#login page
@views.route('/')
def home():
    return render_template("login.html")

# home screen after login
@views.route('/dashboard')
def dashboard():
    return render_template("home.html")

# view account
@views.route('/view-account')
def view_account():
    return render_template("viewAccount.html")

#make deposits
@views.route('/making-deposits')
def create_account():
    return render_template("makeDeposits.html")

#withdraw funds
@views.route('/withdrawing-funds')
def withdraw_funds():
    return render_template("withdrawFunds.html")

#check your balance
@views.route('/checking-balances')
def transfer_funds():
    return render_template("checkBalance.html")

# the admin page
@views.route('/adminPage')
def adminPage():
    return render_template("adminPage.html")


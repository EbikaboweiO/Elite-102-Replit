import sqlite3

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

import sqlite3
from website.models import Transactions, User
# remaking tables in case they didn't work the first time
conn = sqlite3.connect('website/database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                account_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                timestamp TEXT NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                first_name TEXT NOT NULL,
                password TEXT NOT NULL
            )''')

conn.commit()
conn.close()

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST', 'HEAD', 'OPTIONS'])
def login():
    if request.method == 'POST': 
      email = request.form.get('email')
      password = request.form.get('password')

      print(password)

      conn = sqlite3.connect('website/database.db')
      c = conn.cursor()

      c.execute("SELECT * FROM user WHERE email=?", (email,))
      user = c.fetchone()

      #redirects to a different page if the person logging in is an admin
      if email == "admin@gmail.com" and password == "admin":
        return redirect(url_for('views.adminPage'))

      if user and password is not None:
        if check_password_hash(user[3], password):
          flash('Logged in successfully!', category='success')
          return redirect(url_for('views.dashboard'))
        # if password is wrong, but the email is right then it just does this  
        else:
          flash('Incorrect password, try again.', category='error')
      # if it couldn't find the email in the database then it does this    
      else:
        flash('Email does not exist.', category='error')

      conn.close()

    return render_template("login.html")

@auth.route('/logout')
def logout():
    # This just redirects back to the login page 
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=[ 'GET', 'POST'])
def register():
  if request.method == "POST":
    # gets all of the information the user put in
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    conn = sqlite3.connect('website/database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM user WHERE email=?", (email,))
    user = c.fetchone()

    if user:
      #checks if email already exists
      flash('Email already exists.', category='error')
    elif email is not None and len(email) < 4:
      # checks if email is long enough
      flash("Email must be greater than 3 characters.", category='error')
    elif first_name is not None and len(first_name) < 2:
      # checks if first name is long enough
      flash('First name must be greater than 1 character.', category='error')
    elif password1!= password2:
      # if the passwords don't match
      flash("Passwords don't match.", category='error')  
    else:
      if password1 is not None:
        # signs the user up and puts them in the database
        hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
        c.execute("INSERT INTO user (email, first_name, password) VALUES (?,?,?)", 
                  (email, first_name, hashed_password))
        conn.commit()
        flash(f"Account created for {email}!", category='success')
        return redirect(url_for('views.home'))

    conn.close()

  return render_template("signUp.html")
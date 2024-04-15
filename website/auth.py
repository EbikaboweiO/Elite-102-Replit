from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.models import User
from werkzeug.security import generate_password_hash, check_password_hash




auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("base.html")

@auth.route('/sign-up', methods=[ 'GET', 'POST'])
def register():
  if request.method == "POST":
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if email is not None and len(email) < 4:
      flash("Email must be greater than 3 characters.", category='error')
    elif first_name is not None and len(first_name) < 2:
      flash('First name must be greater thn 1 character.', category='error')
    elif password1 != password2:
      flash("Passwords don't match.", category='error')  
    else:
      if password1 is not None:
        new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
        
        from website.__init__ import db

        db.session.add(new_user)
        db.session.commit()
        flash(f"Account created for {email}!", category='success')
        
      
  return render_template("signUp.html")

#  will have access to typical banking functions such as checking balances, making deposits, and withdrawing funds.

# account management, including the creation, modification, and closure of accounts by users or bank administrators.

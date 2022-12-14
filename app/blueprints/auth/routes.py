from. import bp as app
from app import db
from flask import render_template, request,redirect, url_for, flash
from app.blueprints.blog.models import User
from flask_login import login_manager

from flask_login import login_user, logout_user, current_user


# from flask import render_template, request, redirect ,url_for
# from app.models import Car
# from app.blueprints.blog.models import Car

@app.route('/login', methods=["GET", "POST"])
def login():
#Conditional stament to check weather request is a GET OR A POST
    if request.method == 'GET':
        return render_template('login.html')
#If it gets to this point in the functionit its a post request
    email = request.form['email']
    password = request.form['password']

# def check_my_password(self, password):
#         return check_password_hash(self.password, password)

    user=User.query.filter_by(email=email).first()

    #if user doesnt exist
    if user is None:
        flash(f'User with email {email} does not exist.','danger')
        
    elif user.check_my_password(password):
        login_user(user)
        flash(f'welcome back{{first_name}}', 'success')
        return redirect(url_for('main.home'))
    else:
        #user exists but the password is incorrect
        flash("Password incorrect", 'danger')
        

    return render_template('login.html')

    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    # otherwise user is making a post request
    email =request.form['email']
    password =request.form['password']
    confirm_password =request.form['confirmPassword']
    user_name =request.form['username']
    first_name =request.form['firstName']
    last_name =request.form['lastName']

    check_user= User.query.filter_by(email=email).first()

    if check_user is not None:
       flash(f'User with email {email} already exists.', 'danger')

    elif password != confirm_password:
        flash('Passwords do not match.', 'danger')

        
    else:
       
        try:
            new_user = User(email=email, user_name=user_name, password='', first_name=first_name, last_name=last_name)
            new_user.hash_my_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('User created successfully.', 'success')
            return redirect(url_for('auth.login'))
        except:
            flash('there ws an error')

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('auth.login'))  




@app.route('/reset-passowrd', methods=[ "GET","POST" ])
def reset_password():
    if request.method == 'GET':
        return render_template('reset-password.html')

    old_password=request.form['oldPassword']
    new_password=request.form['newPassword']

    if not current_user.check_my_password(old_password):
        Print('Old password not correct', 'danger')

    else:
        current_user.hash_my_password(new_password)
        db.session.add(current_user)
        db.session.commit()
        flash('Password changed successfully', 'success')

    return render_template('reset-password.html')


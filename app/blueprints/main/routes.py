from. import bp as app
from flask import render_template
from flask_login import current_user


@app.route('/')
def home():
    # print(current_user.user_name)
    return render_template('Home.html',user=current_user)

@app.route('/about')
def about():
    return render_template('About.html')
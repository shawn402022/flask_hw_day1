from app import app

from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/blog')
def blog():
    return render_template('Blog.html')

@app.route('/register')
def register():
    return render_template('Register.html')

@app.route('/login')
def login():
    return render_template('Login.html')

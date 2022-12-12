from app import app, db
from flask import render_template, request, redirect ,url_for
from app.models import Car

from flask import render_template

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('About.html')

# @app.route('/blog')
# def blog():
#     return render_template('Blog.html')

# @app.route('/register')
# def register():
#     return render_template('Register.html')

# @app.route('/login')
# def login():
#     return render_template('Login.html')

@app.route('/car')
def cars():
    all_cars = Car.query.all()
    return render_template('cars.html', cars=all_cars)

@app.route('/car/<id>')
def car_by_id(id):
    car= Car.query.get(int(id))
    return render_template('car-single.html', car=car)

@app.route('/create-car',methods=["POST"])
def create_car():
    model =request.form['inputModel']
    make = request.form['inputMake']
    year =request.form['inputYear']
    color = request.form['inputColor']
    price =request.form['inputPrice']
    new_car = Car(model=model, make=make, year=year, color=color, price=price, user_id=1)
    db.session.add(new_car)
    db.session.commit()
    
    return redirect(url_for('cars')) 


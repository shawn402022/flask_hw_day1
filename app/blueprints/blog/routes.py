from. import bp as app
from app import db
from flask import render_template, request, redirect ,url_for,flash
from flask import flash 
from flask_login import current_user, login_required
# from app.models import Car
from app.blueprints.blog.models import Car

@app.route('/car')
@login_required
def cars():
    all_cars = Car.query.all()
    return render_template('cars.html', cars=all_cars)

@app.route('/car/<id>')
@login_required
def car_by_id(id):
    car= Car.query.get(int(id))
    return render_template('car-single.html', car=car)

@app.route('/create-car',methods=["POST"])
@login_required
def create_car():
    model =request.form['inputModel']
    make = request.form['inputMake']
    year =request.form['inputYear']
    color = request.form['inputColor']
    price =request.form['inputPrice']
    new_car = Car(model=model, make=make, year=year, color=color, price=price, user_id=current_user.id)
    db.session.add(new_car)
    db.session.commit()
    flash('created successfully', 'success')
    
    return redirect(url_for('blog.cars')) 


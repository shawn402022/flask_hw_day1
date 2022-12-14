from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(200)) 
    user_name=db.Column(db.String(50), unique=True)
    first_name=db.Column(db.String(50)) 
    last_name=db.Column(db.String(50))


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    year = db.Column(db.Integer)
    color = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.relationship('User',backref='Car')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
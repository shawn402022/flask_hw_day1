from.import bp as app
from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(200)) 
    user_name=db.Column(db.String(50), unique=True)
    first_name=db.Column(db.String(50)) 
    last_name=db.Column(db.String(50))

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)

    def check_my_password(self, password):
        return check_password_hash(self.password, password)


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

def hash_passwords():
    users = User.query.filter(User.id <= 6).all()
    print(users)
    for user in users:
        user.hash_my_password(user.password)
        db.session.add(user)

    db.session.commit()
from src import db
from uuid import uuid4

class Reservation(db.Model):
    __tablename__ = "reservation"
    
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(110), nullable=False)
    second_name = db.Column(db.String(110), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)

    def __init__(self, first_name, second_name, email):
        self.uuid = str(uuid4())
        self.first_name = first_name
        self.second_name = second_name
        self.email = email

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.Text)

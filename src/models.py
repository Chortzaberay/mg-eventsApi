from src import db
from uuid import uuid4

class Reservation(db.Model):
    __tablename__ = "reservation"
    
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(110), nullable=False)
    second_name = db.Column(db.String(110), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)

    def __init__(self, first_name, second_name, email, event_id):
        self.uuid = str(uuid4())
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.event_id = event_id

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.Text)
    reservation = db.relationship("Reservation", backref='events', lazy=True)

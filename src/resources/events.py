from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src.models import Event
from src.schemes.events import EventSchema
from src import db

class EventApi(Resource):
    event_schema = EventSchema()

    def get(self, event_id=None):
        if not event_id:
            events = Event.query.all()
            return self.event_schema.dump(events, many=True), 200
        event = Event.query.filter_by(id=event_id).first()
        return self.event_schema.dump(event), 200

    def post(self):
        try:
            event = self.event_schema.load(
                request.json, 
                session=db.session
            )    
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(event)
        db.session.commit()
        return self.event_schema.dump(event), 201

    def put(self, event_id):
        event = Event.query.filter_by(id=event_id).first()
        if not event:
            return "", 404
        try:
            event = self.event_schema.load(
                request.json,
                session=db.session,
                instance=event,
                partial=True
            )
        except ValidationError as e:
            return {"message": str(e)}, 400
        #db.session.add(event)
        db.session.commit()
        return self.event_schema.dump(event), 201

    def delete(self, event_id):
        event = Event.query.filter_by(id=event_id).first()
        if not event:
            return {"message": "Wrong id or event doesn't exist"}, 400
        db.session.delete(event)
        db.session.commit()
        return {"message": "event deleted"}, 204
        
from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from src.models import Reservation
from src.schemes.reservation import ReservationSchema
from src import db


class ReservationApi(Resource):
    reservation_schema = ReservationSchema()

    def get(self, uuid):
        reservation = Reservation.query.filter_by(uuid=uuid).first()
        if not reservation:
            return "", 404
        return self.reservation_schema.dump(reservation), 200
    
    def post(self):
        try:
            reservation = self.reservation_schema.load(
                request.json,
                session=db.session,
            )
        except ValidationError as e:
            return str(e), 400
        db.session.add(reservation)
        db.session.commit()
        return self.reservation_schema.dump(reservation), 201

    def put(self, uuid):
        reservation = Reservation.query.filter_by(uuid=uuid).first()
        if not reservation:
            return "", 404
        try:
            reservation = self.reservation_schema.load(
                request.json, 
                instance=reservation, 
                session=db.session,
                partial=True,
            )
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(reservation)
        db.session.commit()
        return self.reservation_schema.dump(reservation)

        
    def delete(self, uuid):
        reservation = Reservation.query.filter_by(uuid=uuid).first()
        if not reservation:
            return "", 404
        db.session.delete(reservation)
        db.session.commit()
        return {"message": "Reservation Deleted"}, 204
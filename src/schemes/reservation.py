from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models import Reservation

class ReservationSchema(SQLAlchemyAutoSchema):
    class Meta:
        exclude = ["id"]
        load_instance = True
        model = Reservation
        include_fk = True

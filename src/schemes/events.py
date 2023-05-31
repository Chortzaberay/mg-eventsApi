from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models import Event

class EventSchema(SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        model = Event
        
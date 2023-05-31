from src import api
from src.resources.reservations import ReservationApi
from src.resources.events import EventApi
from src.resources.smoke import SmokeApi


api.add_resource(ReservationApi, "/api/reservation", "/api/reservation/<uuid>")
api.add_resource(EventApi, "/api/event", "/api/event/<event_id>")
api.add_resource(SmokeApi, "/api/smoke")

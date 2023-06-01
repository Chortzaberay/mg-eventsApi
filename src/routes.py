from src import api
from src.resources.reservations import ReservationApi
from src.resources.events import EventApi
from src.resources.smoke import SmokeApi


api.add_resource(ReservationApi, "/api/reservations", "/api/reservations/<uuid>", strict_slashes=False)
api.add_resource(EventApi, "/api/events", "/api/events/<event_id>", strict_slashes=False)
api.add_resource(SmokeApi, "/api/smoke")

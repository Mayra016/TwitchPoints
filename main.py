from Models.auth import Auth
from Models.api_requests import API_requests

authentication = Auth()
api = API_requests()

authentication.getAuth()
authentication.validateToken()

api.watch_events(authentication.TOKEN)


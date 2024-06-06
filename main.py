from Models.auth import Auth
from Models.api_requests import API_requests

authentication = Auth()
api = API_requests()

authentication.getAuth()
authentication.validateToken()
channelName = input("Insert your channel's name")
authentication.getChannelId(channelName)

api.watch_events(authentication.TOKEN, authentication.CHANNEL_ID)


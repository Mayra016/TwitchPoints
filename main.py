from Models.auth import Auth
from Models.api_requests import API_requests
# FALTA EL TOKEN DEL USUARIO PARA MANDARLO EN EL WATCH EVENTS

# APP AUTHENTICATION
authentication = Auth()
api = API_requests()
authentication.getAuth()
authentication.validateToken()

# USER AUTHENTICATION
authentication.getAuthChannel()
authentication.getUserToken()
channelName = input("Insert your channel's name")
authentication.getChannelId(channelName)

# LISTEN TO CHANNEL POINT EVENTS
api.watch_events(authentication.USER_TOKEN, authentication.CHANNEL_ID)

# HANDLE EVENTS

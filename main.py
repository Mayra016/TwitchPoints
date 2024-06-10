from Models.auth import Auth
from Models.api_requests import API_requests

info = "Token \n Access url: https://twitchapps.com/tokengen/  \n Required scopes: channel:read:redemptions"

# APP AUTHENTICATION
authentication = Auth()
api = API_requests()
authentication.getAuth()
authentication.validateToken()

# USER AUTHENTICATION
authentication.getAuthChannel()
channelName = input("Insert your channel's name")
authentication.getChannelId(channelName)
print("Your channel id is: " + authentication.CHANNEL_ID)
print(info)
user_TOKEN = input("Paste your OAuth token: ")

# LISTEN TO CHANNEL POINT EVENTS
api.watch_events(user_TOKEN, authentication.CHANNEL_ID)

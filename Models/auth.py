import os
import requests
import json 
import time
import webbrowser

class Auth():

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    TOKEN = ""
    CHANNEL_ID = ""
    USER_TOKEN = ""

    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.TOKEN = ""

    def getAuth(self):
        header_info = {'Content-Type': 'application/json'}
        AUTH_URL = "https://id.twitch.tv/oauth2/token?client_id=" + self.client_id + "&client_secret=" + self.client_secret + "&grant_type=client_credentials"

        response = requests.post(AUTH_URL, headers=header_info)
        response_JSON = json.loads(response.text)
        self.TOKEN = response_JSON['access_token']

        print(self.TOKEN)

        if response.status_code == 200:
            print('Request erfolgreich!')
            print('Antwort des Servers:')
            print(response.text)
        else:
            print('Fehler bei der Anfrage. Statuscode:', response.status_code)



    def validateToken(self):
        validation_header = {"Authorization": "Bearer " + self.TOKEN}
        validation_response = requests.get("https://id.twitch.tv/oauth2/validate", headers=validation_header)    
        if validation_response.status_code == 200:
            print('Request erfolgreich!')
            print('Antwort des Servers:')
            print(validation_response.text)
        else:
            print('Fehler bei der Anfrage. Statuscode:', validation_response.status_code)


    def getChannelId(self, channel_name):
        URL = "https://api.twitch.tv/helix/users?login=" + channel_name
        header = {
            "Authorization": "Bearer " + self.TOKEN,
            "Client-Id": self.client_id
        }

        response = requests.get(URL, headers=header)
        print("AUTH " + response.text)
        if response.status_code == 200:
            response_JSON = response.json()
            # Überprüfe, ob "data" im JSON-Objekt vorhanden ist
            if "data" in response_JSON:
                self.CHANNEL_ID = response_JSON["data"][0]["id"]
                print(f"Kanal-ID für {channel_name}: {self.CHANNEL_ID}")
            else:
                print("Keine Daten gefunden.")
        else:
            print("Fehler bei der Anfrage:", response.status_code)

    def getUserToken(self):
        URL = "https://id.twitch.tv/oauth2/authorize"
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': "http://localhost:8080/auth",
            'scope': 'channel:manage:polls channel:read:polls openid channel:read:redemptions',
        }
        authorization_url = requests.Request('GET', URL, params=params).prepare().url
        print(f"Bitte öffne diesen Link im Browser und erlaube den Zugriff: {authorization_url}")
        webbrowser.open(authorization_url)

        # Schritt 2: Benutzer gibt den Authorization Code ein
        authorization_code = input("Bitte gib den Authorization Code ein, den du erhalten hast: ")

        # Schritt 3: Austausch des Authorization Codes gegen ein Access Token
        TOKEN_URL = "https://id.twitch.tv/oauth2/token"
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': authorization_code,
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri
        }
        response = requests.post(TOKEN_URL, data=data)
        token_data = response.json()

        if 'access_token' in token_data:
            print("Access Token:", token_data['access_token'])
        else:
            print("Fehler beim Abrufen des Tokens:", token_data)


    def getAuthChannel(self):
        header_info = {'Content-Type': 'application/json'}
        AUTH_URL = "https://id.twitch.tv/oauth2/token?client_id=" + self.client_id + "&client_secret=" + self.client_secret + "&grant_type=client_credentials"

        response = requests.post(AUTH_URL, headers=header_info)
        print("AUTH CHANNEL " + response.text)
        response_JSON = json.loads(response.text)
        self.USER_TOKEN = response_JSON['access_token']

        print(self.TOKEN)

        if response.status_code == 200:
            print('Request erfolgreich!')
            print('Antwort des Servers:')
            print(response.text)
        else:
            print('Fehler bei der Anfrage. Statuscode:', response.status_code)


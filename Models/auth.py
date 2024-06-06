import os
import requests
import json 

class Auth():

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    TOKEN = ""
    CHANNEL_ID = ""

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

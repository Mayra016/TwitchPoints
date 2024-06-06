import requests 
import json 
import os

class API_requests():
    client_id = os.getenv("CLIENT_ID")

    def watch_events(self, TOKEN, CHANNEL_ID):
        WATCH_URL = "wss://pubsub-edge.twitch.tv"
        payload = {
            "type": "LISTEN",
            "nonce": "44h1k13746815ab1r2",
            "data": {
                "topics": ["channel-points-channel-v1." + CHANNEL_ID],
                "auth_token": "cfabdegwdoklmawdzdo98xt2fo512y"
            }
        }

        payload_json = json.dumps(payload)
        watch_headers = {'Content-Type': 'application/json'}

        watch_request = requests.get(WATCH_URL, data=payload_json, headers=watch_headers)
        print(watch_request.text)

import requests 
import json 
import os
import websocket

class API_requests():
    client_id = os.getenv("CLIENT_ID")

    def watch_events(self, TOKEN, CHANNEL_ID):
        print("Token: " + TOKEN)
        print("cHANNEL: " + CHANNEL_ID)
        WATCH_URL = "wss://pubsub-edge.twitch.tv"

        def on_message(ws, message):
            print(message)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")

        def on_open(ws):
            print("### open ###")
            payload = {
                "type": "LISTEN",
                "nonce": "44h1k13746815ab1r2",
                "data": {
                    "topics": ["channel-points-channel-v1." + CHANNEL_ID],
                    "auth_token": TOKEN
                }
            }
            ws.send(json.dumps(payload))

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(WATCH_URL,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.on_open = on_open
        ws.run_forever()

import requests 
import json 
import os
import websocket

from Services.ClickEventsService import ClickEventsService
from Services.KeyboardEvents import KeyboardEventsService

class API_requests():
    client_id = os.getenv("CLIENT_ID")

    def watch_events(self, TOKEN, CHANNEL_ID):
        print("Token: " + TOKEN)
        print("cHANNEL: " + CHANNEL_ID)
        WATCH_URL = "wss://pubsub-edge.twitch.tv"

        def on_message(ws, message):
            print("Received message: " + message)
            message_json = json.loads(message)

            if message_json.get("type") == "MESSAGE":
                data = message_json.get("data", {})
                message_content = data.get("message")
                print("Message Content:", message_content)

                message_content_json = json.loads(message_content)
                redemption = message_content_json.get("data", {}).get("redemption", {})
                reward = redemption.get("reward", {})
                reward_title = reward.get("title", "")
                print("Reward Title:", reward_title)
                if "click" in reward_title:
                    click = ClickEventsService(reward_title)

                if "press" in reward_title:
                    press = KeyboardEventsService(reward_title)

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

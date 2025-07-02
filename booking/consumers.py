import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BookingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("booking_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("booking_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')

        await self.channel_layer.group_send(
            "booking_group",
            {
                "type": "booking_message",
                "message": message,
            }
        )

    async def booking_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))

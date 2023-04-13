import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room, Message
from django.contrib.auth import get_user_model
import base64

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']

        if message_type == 'text':
            message = data['message']
            username = data['username']
            room = data['room']

            await self.save_message(username, room, message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message_type': 'text',
                    'message': message,
                    'username': username
                }
            )
        elif message_type == 'image':
            image_data = data['image']
            username = data['username']
            room = data['room']

            await self.save_image(username, room, image_data)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message_type': 'image',
                    'image': image_data,
                    'username': username
                }
            )

    async def chat_message(self, event):
        message_type = event['message_type']

        if message_type == 'text':
            message = event['message']
            username = event['username']

            await self.send(text_data=json.dumps({
                'message_type': 'text',
                'message': message,
                'username': username
            }))
        elif message_type == 'image':
            image_data = event['image']
            username = event['username']

            await self.send(text_data=json.dumps({
                'message_type': 'image',
                'image': image_data,
                'username': username
            }))

    @sync_to_async
    def save_image(self, username, room, image_data):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        # Decode the base64-encoded image data
        image_data = base64.b64decode(image_data)

        Message.objects.create(user=user, room=room, image=image_data)

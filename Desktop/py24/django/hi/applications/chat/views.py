from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from channels.layers import get_channel_layer
from asgiref.sync import sync_to_async
from .models import Room, Message
import json

User = get_user_model()
channel_layer = get_channel_layer()


class RoomList(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        data = [{'name': room.name, 'slug': room.slug} for room in rooms]
        return Response(data)


class RoomDetail(APIView):
    def get(self, request, slug):
        try:
            room = Room.objects.get(slug=slug)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        messages = Message.objects.filter(room=room)[0:25]
        data = {
            'name': room.name,
            'slug': room.slug,
            'messages': [{'content': message.content, 'username': message.user.username} for message in messages]
        }
        return Response(data)

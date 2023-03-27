from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Message, Room
from applications.chat.serializers import ChatSerializer, ChatNotificationSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .send_mail import send_chat_mail
from ..likedislike.models import LikeDislike

User = get_user_model()
channel_layer = get_channel_layer()

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})



# class ChatNotificationAPIView(GenericAPIView):
#     serializer_class = ChatNotificationSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         chat = serializer.save()
#
#         user = LikeDislike.objects.filter(user=chat.user, is_like=True).values_list('user__email', flat=True)
#         if user:
#             send_chat_mail(user)
#
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             f"user_{chat.user.id}",
#             {
#                 "type": "chat_notification",
#                 "message": "New chat notification received!",
#                 "chat_id": chat.id
#             }
#         )
#
#         data = serializer.data
#         message = 'chat notification successfully!'
#         response = {
#             'data': data,
#             'message': message
#         }
#         return Response(response, status=status.HTTP_201_CREATED)
#
#
# class ChatViewSet(ModelViewSet):
#     serializer_class = ChatSerializer
#     # permission_classes = [IsAuthenticated]
#
#     def list(self, request, user_id=None):
#         user = get_object_or_404(User, id=user_id)
#         chats = Chat.objects.filter(user=user) | Chat.objects.filter(user=user)
#         serializer = ChatSerializer(chats, many=True)
#         return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#
#         chat = serializer.save()
#
#         if 'image' in request.FILES:
#             chat.image = request.FILES['image']
#             chat.save()
#
#
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             f"user_{chat.user.id}",
#             {
#                 "type": "chat_message",
#                 "message": "New chat message received!",
#                 "chat_id": chat.id
#             }
#         )
#
#         data = serializer.data
#         message = 'chat created successfully!'
#         response = {
#             'data': data,
#             'message': message
#         }
#         return Response(response, status=status.HTTP_201_CREATED)
#
#     def delete(self, request, user_pk):
#         user = get_object_or_404(User, pk=user_pk)
#         chats = Chat.objects.filter(user=user)
#         chats.delete()
#         message = 'chat history deleted successfully!'
#         response = {
#             'message': message
#         }
#         return Response(response, status=status.HTTP_200_OK)
#


































# class ChatNotificationAPIView(APIView):
#     serializer_class = ChatNotificationSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = serializer.data
#         message = 'chat notification successfully!'
#         response = {
#             'data': data,
#             'message': message
#         }
#         return Response(response, status=status.HTTP_201_CREATED)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
#
# class ChatViewSet(ModelViewSet):
#     serializer_class = ChatSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, user_id=None):
#         user = get_object_or_404(User, id=user_id)
#         chats = Chat.objects.filter(user=user) | Chat.objects.filter(user=user)
#         serializer = ChatSerializer(chats, many=True)
#         return Response(serializer.data)
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#
#         chat = serializer.save(user=self.request.user)
#
#         if 'image' in request.FILES:
#             chat.image = request.FILES['image']
#             chat.save()
#
#         data = serializer.data
#         message = 'chat notification successfully!'
#         response = {
#             'data': data,
#             'message': message
#         }
#         return Response(response, status=status.HTTP_201_CREATED)
#
#     def delete(self, request, user_pk):
#         user = get_object_or_404(User, pk=user_pk)
#         chats = Chat.objects.filter(user=user)
#         chats.delete()
#         message = 'chat history deleted successfully!'
#         response = {
#             'message': message
#         }
#         return Response(response, status=status.HTTP_200_OK)

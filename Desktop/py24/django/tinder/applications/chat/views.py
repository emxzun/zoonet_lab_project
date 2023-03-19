from rest_framework.viewsets import ModelViewSet

from applications.chat.models import Message
from applications.chat.serializers import ChatSerializer, MessageSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ChatViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = ChatSerializer

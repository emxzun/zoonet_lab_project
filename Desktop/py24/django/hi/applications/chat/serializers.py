from rest_framework import serializers
from applications.chat.send_mail import send_chat_mail
from applications.chat.models import Chat, Block
from django.contrib.auth import get_user_model

from applications.likedislike.models import LikeDislike

User = get_user_model()

class ChatSerializer(serializers.ModelSerializer):
    recipient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    block_user = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all(), required=False, allow_null=True, default=None)

    class Meta:
        model = Chat
        fields = ['recipient', 'sender', 'block_user']

    def create(self, validated_data):
        sender = validated_data.get('sender')
        recipient = validated_data.get('recipient')
        block_user = validated_data.get('block_user', None)

        if not LikeDislike.objects.filter(recipient=recipient, sender=sender, is_like=True).exists():
            raise serializers.ValidationError('Recipient has not liked the sender')

        if LikeDislike.objects.filter(sender=recipient, recipient=sender, is_like=False):
            raise serializers.ValidationError('sender has been blocked by recipient')

        if Chat.objects.filter(sender=block_user, recipient=block_user).exists():
            raise serializers.ValidationError('you have blocked')

        send_chat_mail(recipient.email)
        chat = Chat.objects.create(sender=sender, recipient=recipient, block_user=block_user)
        return chat

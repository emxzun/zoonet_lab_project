from django.core.mail import send_mail
from rest_framework import serializers
from applications.chat.models import Message
from django.contrib.auth import get_user_model
from applications.likedislike.models import LikeDislike

User = get_user_model()

class ChatNotificationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = validated_data.get('user')
        block_user = validated_data.get('block_user', None)

        if not LikeDislike.objects.filter(user=user, is_like=True).exists():
            raise serializers.ValidationError('User has not liked the sender')

        if LikeDislike.objects.filter(user=user, is_like=False):
            raise serializers.ValidationError('you have been blocked by user')

        if Message.objects.filter(user=validated_data.get('user')).exists():
            raise serializers.ValidationError('you have blocked')

        liked_users = LikeDislike.objects.filter(user=user, is_like=True).values_list('user__email', flat=True)
        send_mail(
            'New Chat Notification',
            'A new chat has been created by {}'.format(user.username),
            'kadirbekova43@gmail.com',
            liked_users,
            fail_silently=False,
        )
        chat = Message.objects.create(user=user, block_user=block_user)
        return chat

class ChatSerializer(serializers.ModelSerializer):
    block_users=serializers.PrimaryKeyRelatedField(queryset=Message.objects.all(), required=False, allow_null=True, default=None)
    class Meta:
        model = Message
        fields = ['user', 'image','message', 'block_users']













#
# class ChatNotificationSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     block_user = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all(), required=False, allow_null=True, default=None)
#
#     class Meta:
#         model = Chat
#         fields = ['user', 'block_user', ]
#
#     def create(self, validated_data):
#         user = validated_data.get('sender')
#         block_user = validated_data.get('block_user', None)
#
#         if not LikeDislike.objects.filter(user=User, is_like=True).exists():
#             raise serializers.ValidationError('User has not liked the sender')
#
#         if LikeDislike.objects.filter(user=User, is_like=False):
#             raise serializers.ValidationError('You has been blocked by another user')
#
#         if Chat.objects.filter(user=block_user).exists():
#             raise serializers.ValidationError('you have blocked')
#
#         send_chat_mail(User.email)
#         chat = Chat.objects.create(user=User, block_user=block_user)
#         return chat
#
# class ChatSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(required=False)
#     class Meta:
#         model = Chat
#         fields = ['user', 'block_user', 'type', 'message', 'image']
#



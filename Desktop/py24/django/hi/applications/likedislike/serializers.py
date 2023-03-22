from rest_framework import serializers
from applications.likedislike.models import LikeDislike
from applications.likedislike.send_mail import send_like_mail
from django.contrib.auth import get_user_model

User = get_user_model()

class LikeDislikeSerializer(serializers.ModelSerializer):
    recipient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = LikeDislike
        fields = ['sender', 'recipient', 'is_like', 'is_dislike']

    def create(self, validated_data):
        request = self.context.get('request')
        recipient = validated_data['recipient']
        send_like_mail(recipient.email)
        like = LikeDislike.objects.create(sender=request.user, recipient=recipient, is_like=True)
        return like
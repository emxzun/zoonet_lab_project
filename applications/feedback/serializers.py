from django.contrib.auth import get_user_model
from rest_framework import serializers
from applications.feedback.models import Feedback

User = get_user_model()

class FeedbackSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='username.username')

    class Meta:
        model = Feedback
        fields = ['username', 'content']

    def create(self, validated_data):
        username = validated_data.pop('username')
        user = User.objects.get(username=username)
        feedback = Feedback.objects.create(username=user, **validated_data)
        return feedback
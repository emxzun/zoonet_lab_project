from rest_framework import serializers
from django.contrib.auth import get_user_model

from applications.announcement.models import Announcement


User = get_user_model()


class AnnouncementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Announcement
        fields = '__all__'

    
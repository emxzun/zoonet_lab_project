from rest_framework import serializers
from django.contrib.auth import get_user_model

from applications.announcement.models import Announcement


User = get_user_model()


class AnnouncementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Announcement
        fields = ['description', 'images', 'phone', 'price', 'category', 'location']

    def create(self, validated_data):
        request = self.context.get('request')
        images = validated_data['images']
        description = validated_data['description']
        phone = validated_data['phone']
        price = validated_data['price']
        category = validated_data['category']
        location = validated_data['location']
        announcement = Announcement.objects.create(user=request.user, images=images, description=description, phone=phone, price=price, category=category, location=location)
        return announcement   

    

    
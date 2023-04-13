from rest_framework import serializers
from django.contrib.auth import get_user_model

from applications.announcement.models import Announcement, ImageAnnouncement


User = get_user_model()

class ImageAnnouncementSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Announcement
        fields = ('id', 'image', 'image_thumbnail')

class AnnouncementSerializer(serializers.ModelSerializer):
    images = ImageAnnouncementSerializer(many=True, read_only=True)
    image_files = serializers.ListField(child=serializers.FileField(), write_only=True)
    
    class Meta:
        model = Announcement
        fields = ['description', 'images', 'phone', 'price', 'category', 'location']

    def create(self, validated_data):
        request = self.context.get('request')
        description = validated_data['description']
        phone = validated_data['phone']
        price = validated_data['price']
        category = validated_data['category']
        location = validated_data['location']
        announcement = Announcement.objects.create(user=request.user, description=description, phone=phone, price=price, category=category, location=location)
        
        for image_data in request.data.getlist('images'):
            ImageAnnouncement.objects.create(announcement=announcement, image=image_data)

        return announcement   
    


    

    
from rest_framework import serializers

from applications.announcement.models import Announcement, ImageAnnouncement

class ImageAnnouncementSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ImageAnnouncement
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    images = ImageAnnouncementSerializer(many=True, required=True)

    class Meta:
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        announcement = Announcement.objects.create(user=user, **validated_data)
        files_data = request.FILES
        for image in files_data.getlist('images'):
            print(image)
            ImageAnnouncement.objects.create(announcement=announcement, image=image)

        return announcement
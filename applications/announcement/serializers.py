from rest_framework import serializers

from applications.announcement.models import Announcement, ImageAnnouncement


class ImageAnnouncementSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ImageAnnouncement
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    images = ImageAnnouncementSerializer(many=True, read_only=True)
    user = serializers.EmailField(required=False, read_only=True)

    class Meta:
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        announcement = Announcement.objects.create(user=user, **validated_data)
        files_data = request.FILES
        if len(files_data.getlist('images'))>10:
               raise serializers.ValidationError('Нельзя отправлять больше 10 фотографий')
        else:
            for image in files_data.getlist('images'):
                ImageAnnouncement.objects.create(announcement=announcement, image=image)

        return announcement

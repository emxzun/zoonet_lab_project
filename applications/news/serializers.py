from rest_framework import serializers
from applications.news.models import News


class NewsSerializers(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'

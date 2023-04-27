from rest_framework import serializers
from applications.news.models import News


class NewsSerializers(serializers.ModelSerializer):

    class Meta:
        model = News
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = '__all__'
>>>>>>> 489992a1922f2266d32ed71161681565cfd08ae0

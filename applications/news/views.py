<<<<<<< HEAD
=======
from django.shortcuts import render

>>>>>>> 489992a1922f2266d32ed71161681565cfd08ae0
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from applications.news.models import News
from applications.news.serializers import NewsSerializers


class NewsAPIView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = [IsAdminUser]

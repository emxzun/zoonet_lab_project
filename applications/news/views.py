from django.shortcuts import render

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from applications.news.models import News
from applications.news.serializers import NewsSerializers


class NewsAPIView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = [IsAdminUser]
